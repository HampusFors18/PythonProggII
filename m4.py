"""
Solutions to exam tasks for modul 4
Name:Hampus Naumanen
Code:AX-0055-ZCW
"""

# A9
def toeplitz(n):
    """En metod som returnerar en lista som motsvarar en 
    Toeplitz-matris av storlek nxn"""
    matrix = [[i-j for j in range(n)] for i in range(n)]
    return matrix

# A10
def get_balance(index):
    """Denna metod öppnar customers.json och 
    returnerar fältet 'balance' för personen med det givna indexet.
    Låt denna metod vara som den är.
    Notera att '$' and ',' rensas bort från 'balance' """
    import json
    with open('customers.json') as f:
        data = json.load(f)
        return data[index]['balance'].replace('$', '').replace(',', '')


def get_minmax_balance(indexes):
    """Metod som kör get_balance parallellt för varje index i listan indexes.
    Metoden ska sedan returnera det minsta och största värdet av resultaten från get_balance."""
    
    from concurrent import futures as f
    list_balance = []
    with f.ThreadPoolExecutor() as ex:
        results = ex.map(get_balance, indexes)
        for a in results:
            list_balance.append(a)
        
    balance_tuple = (min(list_balance), max(list_balance))
    return balance_tuple
    
    


# B4

def convert_images():
    """Metod som konverterar alla .png till .jpg i katalogen som programmet körs i
    Det är ok att lägga till metoder och ha globala variabler"""

    pass # Ta bort pass och skriv din kod här

def main():
    print('Test av A9 (jämför med exemplen i tentamens-uppgiften)')
    import numpy
    print(numpy.array(toeplitz(3)))
    print(numpy.array(toeplitz(4)))
    print(numpy.array(toeplitz(5)))


    print('\nTest av A10')
    print(get_minmax_balance([1,5,9]), "  Korrekt ('1335.46', '2319.84')")
    print(get_minmax_balance(range(10)), "  Korrekt ('1335.46', '3513.32')")


    print('\nKör koden i B4')
    convert_images()

if __name__ == "__main__":
    main()
    print('Over and out')
