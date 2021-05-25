"""
This file contains a simplified version of the calculator in the
second assignment.
It does not, for example, handle variables.
The TokenizeWrapper is included in this file.
"""

import io
import math
from tokenize import TokenError
import tokenize


class TokenizeWrapper:
    def __init__(self, line):
        self.line = line
        self.tokens = tokenize.generate_tokens(io.StringIO(line).readline)
        self.current = next(self.tokens)
        self.previous = 'START'

    def __str__(self):
        return self.current[1]

    def get_current(self):
        if self.current[0] > 0:
            return self.current[1]
        else:
            return 'NO MORE TOKENS'

    def get_previous(self):
        return self.previous

    def next(self):
        # The return value is mainly intended for debugging purposes
        if self.has_next():
            self.previous = self.current[1]
            self.current = next(self.tokens)
            return self.current
        else:
            return (0, 'EOS')

    def is_number(self):
        return self.current[0] == 2

    def is_name(self):
        return self.current[0] == 1

    def is_newline(self):
        return self.current[0] == 4

    def is_at_end(self):
        return self.current[0] == 0 or self.current[0] == 4

    def has_next(self):
        return self.current[0] != 0 and self.current[0] != 4


class SyntaxException(Exception):
    def __init__(self, arg):
        self.arg = arg


class EvaluationException(Exception):
    def __init__(self, arg):
        self.arg = arg


functions = {'sin': math.sin, 'cos': math.cos,
             'exp': math.exp, 'log': math.log}


def assignment(wtok):
    result = expression(wtok)
    # Assignments is not implemented and you do not have to do it.
    return result


def expression(wtok):
    result = term(wtok)
    while wtok.get_current() in ['+', '-']:
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok)
        else:
            wtok.next()
            result = result - term(wtok)
    return result


def term(wtok):
    result = factor(wtok)
    while wtok.get_current() in ['*', '/']:
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok)
        else:
            wtok.next()
            try:
                result = result / factor(wtok)
            except ZeroDivisionError:
                raise EvaluationException("Division by zero")
    return result


def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok)
        if wtok.get_current() != ')':
            raise SyntaxException("Expected ')'")
        else:
            wtok.next()
            return result
    elif wtok.get_current() == '-':
        wtok.next()
        return -factor(wtok)
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
        return result
    elif wtok.get_current() in functions:
        return function_handler(wtok)
    else:
        raise SyntaxException(
            "Expected number, function name, '-' or '('")


def function_handler(wtok):
    name = wtok.get_current()
    wtok.next()
    if wtok.get_current() != '(':
        raise SyntaxException("Expected '(' after function name")
    arg = factor(wtok)
    try:
        return functions[name](arg)
    except ValueError:
        raise EvaluationException(
            f"Illegal argument to function  '{name}({arg})'")


def statement(wtok):
    if wtok.get_current() == 'quit':
        print('Bye')
        exit()
    else:
        result = assignment(wtok)
        if not wtok.is_at_end():
            raise SyntaxException('Expected end of line or an operator')
        return result


def run(line=''):
    try:
        while line == '':
            line = input("> ")
        wtok = TokenizeWrapper(line)
        return statement(wtok)
    except SyntaxException as e:
        print(f'*** Error: {e.arg}. At {wtok.get_current()} just after {wtok.get_previous()}')
        return 'Error'
    except TokenError as te:
        print('*** Error: Unbalanced parentheses')
        return 'Error'
    except EvaluationException as e:
        print(f' *** Error: {e.arg}')
        return 'Error'


if __name__ == "__main__":
    """Run this file to test your implementations in the terminal. 
       The code below will only run if this is the main file running.
       Write 'quit' to exit the calculator."""

    print("Numerical calculator")

    while True:
        print('Result: ', run())