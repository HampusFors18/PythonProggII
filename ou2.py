"""
Solutions to module 2 - A calculator
Student: Hampus Naumanen
Mail: hampus.naumanen.94@hotmail.com
Reviewed by: Bruse
Reviewed date: 24/5
"""



from tokenize import TokenError
from p2tokenizer import TokenizeWrapper
import math
from statistics import mean


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        
class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        
class FileError(Exception):
    def __init__(self, arg):
        self.arg = arg
        
class Function_name_Error(Exception):
    def __init__(self, arg):
        self.arg = arg
    

#memory = {0:0, 1:1}
def fib_mem(n, memory):
    '''
    
    
    Parameters
    ----------
        n (int) : A positive integer
        memory (dict) : Dictionary of two previous Fibonacci numbers
        
    Raises
    ------
        EvaluationError : When a non-positive integer is evaluated

    Returns
    -------
        memory [n] (int): Integer of the value of the n:th Fibonacci number
    '''
    if n < 0 or not n.is_integer():
         raise EvaluationError(f"Argument to fib is '{n}'" + " Must be integer >=0.")
    elif n in memory:
        return memory[n]
    else:
        memory[n] = fib_mem(n-1, memory) + fib_mem(n-2, memory)
        return memory[n]
    
            
# def fib(n):
#     if n < 0 or not n.is_integer():
#         raise EvaluationError(f"Argument to fib is '{n}'" + " Must be integer >=0.")
#     elif n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

def fac(n):
    '''
    

    Parameters
    ----------
        n (int) : A positive integer

    Raises
    ------
        EvaluationError : When a non-positive integer is evaluated

    Returns
    -------
        n*fac(n-1) (int) : The n:th faculty recursively

    '''
    if n < 0 or not n.is_integer():
        raise EvaluationError(f"Argument to fac is '{n}'" + " Must be integer >=0.")
    else:
        if n==0:
            return 1
        else:
            return n*fac(n-1)


dict_functions = {
        "sin": math.sin,
        "cos": math.cos, 
        "exp": math.exp, 
        "log": math.log,
        "mean": mean,
        "max": max,
        "fib": fib_mem,
        "fac": fac,
        }

dict_variables = {"ans": 0, "E": math.e, "PI": math.pi, "FuncName": "init", "FuncArg": 0}


        

def arglist(wtok):
    '''
    

    Parameters
    ----------
    wtok : Token-generated string

    Raises
    ------
    SyntaxError : Missing ',' or ')' for the argument
    TokenError : Unbalanced parantheses

    Returns
    -------
    list_of_values (list) : List of values of the passed arguments

    '''
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok)
        list_of_values = []
        list_of_values.append(result)
        while wtok.get_current() == ',':
            wtok.next()
            result = assignment(wtok)
            list_of_values.append(result)
        if wtok.get_current() == ')':
            wtok.next()
        else:
            raise SyntaxError("Expected ',' or ')'")
    else:
        raise TokenError               #Return list not value
    if len(list_of_values) == 1:
        dict_variables["FuncArg"] = list_of_values[0]
        return list_of_values[0]
    else:
        dict_variables["FuncArg"] = list_of_values
        return list_of_values
    
    
    
def assignment(wtok):
    '''
    -----Beskrivning-----

    Parameters
    ----------
    wtok : Token-generated string

    Raises
    ------
    SyntaxError : If '=' is not followed by name or variable

    Returns
    -------
    result : Result of an assignment

    '''
    result = expression(wtok)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            dict_variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("Expected name or variable after '='")
    return result
        
        
def expression(wtok):
    '''
    

    Parameters
    ----------
    wtok : Token-generated string

    Returns
    -------
    result : Result of addition or subtraction

    '''
    result = term(wtok)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok)
        else:
            wtok.next()
            result = result - term(wtok)
    return result


def term(wtok):
    '''
    

    Parameters
    ----------
    wtok : Token-generated string

    Raises
    ------
    EvaluationError : Division by zero

    Returns
    -------
    result : Result of division or multiplication

    '''
    result = factor(wtok)
    while wtok.get_current() == "*" or wtok.get_current() == "/":
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok)
        else:
            wtok.next()
            try:
                result = result / factor(wtok)
            except ZeroDivisionError:
                raise EvaluationError("Division by zero")
    return result


def factor(wtok):
    '''
    

    Parameters
    ----------
    wtok : Token-generated string

    Raises
    ------
    TokenError : Unbalanced parantheses
    EvaluationError : If variable is undefined
    SyntaxError : If a number, word or '(' is expected

    Returns
    -------
    result : Result of function, number or negation

    '''
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok)       #Assignment
        if wtok.get_current() == ')':
            wtok.next()
        else:
            raise TokenError
    elif wtok.get_current() in dict_functions:
        dict_variables["FuncName"] = wtok.get_current()
        result = function_name(wtok)
    elif wtok.is_name():
        if wtok.get_current() in dict_variables:
            dict_variables["FuncName"] = wtok.get_current()
            result = dict_variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(f"Undefined variable '{wtok.get_current()}'")
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok)
        
    else:
        raise SyntaxError("Expected number, word or '('")
    return result


def function_name(wtok):
    '''
    

    Parameters
    ----------
    wtok : Token-generated string

    Raises
    ------
    Function_name_Error : The argument of the function is constructed wrong, or with values that can't be evaluated'

    Returns
    -------
    dict_functions : Evaluation of the function

    '''
    wtok.next()
    try:
        if wtok.get_previous() == 'fib':
            memory = {0:0, 1:1}
            return dict_functions[wtok.get_previous()](arglist(wtok), memory)
        else:
            return dict_functions[wtok.get_previous()](arglist(wtok))
    except ValueError:
        raise Function_name_Error("Bad value of argument")
    except TypeError:
        raise Function_name_Error("Argument to function is bad")


def readFromFile(filename):
    '''
    

    Parameters
    ----------
    filename : The name of the file

    Raises
    ------
    FileError : If file is not found

    Returns
    -------
    list_of_lines (list) : List of the lines from the file

    '''
    list_of_lines = []
    try:
        testFile = open(filename, "r")
        for line in testFile:                   #Appending lines from file to list
            list_of_lines.append(line.strip())
        testFile.close()
        return list_of_lines
    except FileNotFoundError:
        raise FileError("Try another file name!")


def main():
    print("Calculator version 0.1")
    list_of_lines_from_file = []
    while True:
        if len(list_of_lines_from_file) == 0:
            line = input("Input : ")
            wtok = TokenizeWrapper(line)
        else:
            print("Input : " + list_of_lines_from_file[0])
            wtok = TokenizeWrapper(list_of_lines_from_file.pop(0))
        try:
            if wtok.get_current() == 'quit':
                break
            elif wtok.get_current() == 'vars':
                print(dict_variables)
            elif wtok.get_current() == 'file':
                calcTestFile = "test1.txt"
                list_of_lines_from_file = readFromFile(calcTestFile)
            else:
                result = assignment(wtok)       #Update ans
                dict_variables["ans"] = result
                if wtok.is_at_end():
                    print('Result: ', result)
                else:
                    raise SyntaxError('Unexpected token')
                
        except SyntaxError as se:
            print("*** Syntax error: ", se.arg)
            print(f"Error ocurred at token '{wtok.get_current()}'" + \
                  f" just after '{wtok.get_previous()}'")
            
        except TokenError:
            print('*** Syntax error: Unbalanced parentheses')
            
        except EvaluationError as se:
            print("*** Evaluation error: ", se.arg)
            print(f"Error ocurred at token '{wtok.get_current()}'" + \
                  f" just after '{wtok.get_previous()}'")
            
        except FileError as se:
            print("*** File not found error: ", se.arg)
            
        except Function_name_Error as se:
            print("*** Evaluation error: ", se.arg)
            print(f"Error ocurred at token '{dict_variables['FuncArg']}'" + \
                  f" just after '{dict_variables['FuncName']}'")
          
    print('Bye!')
    

if __name__ == "__main__":
    main()


   