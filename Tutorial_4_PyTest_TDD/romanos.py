def convertToRomans(entero):
    numeros = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L','XL','X','IX','V','IV','I']

    numeral = ''
    i = 0
    
    while entero > 0:
        for _ in range(entero // numeros[i]):
            numeral += numerales[i]
            entero -= numeros[i]

        i += 1

    return numeral

# Con upper() la letra siempre sera pasada a mayuscula
#number = int(input("Numero Romano: "))
#print( "Numero Arabigo:", convertToRomans(number))