###################################################################
# Elaborado por: Alejandro Madrigal y Daniel Campos
# Fecha de creación: 02/09/2023 Hora: 5:33 pm
# Última edición: 03/09/2023 Hora:
# Versión: 3.11.4
###################################################################
from funciones import *
# def de funciones
# 1
def elevarNumeroAux(n, exp):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int) and isinstance(exp, int):
        if n < 0 or exp < 0:
            return print("Ambos números deben ser enteros positivos mayores o iguales que cero")
        else:
            elevarNumero(n, exp)
    return ""
def opcionelevarNumero(n, exp):
    """
    F: Entradas de la función elevar número
    E (int): Valor de la base y el exponente
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Elevar un número.")
            n = int(input("Digite el valor de la base: "))
            exp = int(input("Digite el valor del exponente: "))
            print(elevarNumeroAux(n, exp))
            return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# 2
def obtenerSumatoriaAux(n):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int) == True:
        if n > 0:
            obtenerSumatoria(n)
        else:
            print("Debe ser mayor que 0.")
    return ""
def opcionobtenerSumatoria(n):
    """
    F: Entradas de la función obtener sumatoria
    E (int): Valor del límite que llega la sumatoria
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print(
                "Escriba un número límite y calcula el valor de la sumatoria del número indicado y los números anteriores al cuadrado.")
            n = int(input("Digite un número límite de la sumatoria: "))
            print(obtenerSumatoriaAux(n))
            return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# 3
def esNumeroPrimoAux(n):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int) == True:
        if n > 0:
            esNumeroPrimo(n)
        else:
            print("Debe ser mayor que 0.")
    return ""
def opcionoesNumeroPrimo(n):
    """
    F: Entradas de la función número primo
    E (int): Valor numérico a revisar
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Saber si un valor es primo o no.")
            n = int(input("Digite un número: "))
            print(esNumeroPrimoAux(n))
            return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# 4
def sumarMultiplosAux(n, mult):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int) == True and isinstance(mult, int):
        if n > 0 and mult > 0:
            sumarMultiplos(n, mult)
        else:
            return "Debe ser mayor que 0."
    return ""
def opcionsumarMultilpos(n, mult):
    """
    F: Entradas de la función sumar múltiplos
    E (int): Valor de la base y el exponente
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print(
                "Digite número y un dígito, y calcula la suma de todos sus dígitos, siempre que sean múltiplos del dígito especificado")
            n = int(input("Digite un número: "))
            mult = int(input("Digite un dígito: "))
            print(sumarMultiplosAux(n, mult))
            return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# 5
def obtenerFibonacciAux(n):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int) == True:
        if n >= 1:
            obtenerFibonacci(n)
        else:
            print("Debe ser mayor o igual que 1.")
    return ""
def opcionobtenerFibonacci(n):
    """
    F: Entradas de la función bbtener Fibonacci
    E (int): Valor numérico a revisar
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Obtener la sucesión de Fibonacci es la sucesión infinita de números naturales del n-ésimo número.")
            n = int(input("Digite un el número: "))
            print(obtenerFibonacciAux(n))
            print(obtenerFibonacci(n))
            return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# 6
def esPerfectoAux(n):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int) == True:
        if n > 0:
            esPerfecto(n)
        else:
            return print("Debe ser mayor a 0.")
        return ""
def opcionesPerfecto(n):
    """
    F: Entradas de la función número perfecto
    E (int): Valor de la base y el exponente
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print(
                "Número perfecto (Un número perfecto es un número natural que es igual a la suma de sus divisores propios positivos).")
            n = int(input("Digite un número: "))
            print(esPerfectoAux(n))
            return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# 7
def obtenerMCDaux(n, m):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n and m, int) == True:
        if n > 0 and m>0:
            obtenerMCD(n, m)
        else:
            return print("Deben ser mayores a 0.")
    return ""
def opcionobtenerMCD(n, m):
    """
    F: Entradas de la función obtener el máximo común divisor
    E (int): Valor de la base y el exponente
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Obtener el máximo común divisor.")
            n = int(input("Digite un número: "))
            m = int(input("Digite otro número: "))
            print(obtenerMCDaux(n, m))
            return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# 8
def obtenerMCMaux(n, m):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n and m, int) == True:
        if n > 0 and m>0:
            obtenerMCM(n, m)
        else:
            return print("Deben ser mayores a 0.")
    return ""
def opcionobtenerMCM(n, m):
    """
    F: Entradas de la función obtener el mínimo común divisor
    E (int): Valor de la base y el exponente
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Obtener el mínimo común múltiplo.")
            n = int(input("Digite un número: "))
            m = int(input("Digite otro número: "))
            print(obtenerMCMaux(n, m))
            return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# menú
def menuAux():
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Opción del menú seleccionada
    S: Función seleccionada
    """

def menu():
    """
    F: Elegir la función que se desea utilizar
    E (int): Número asignado a la función
    S (int): Entradas para la función
    """
    print("*********************************")
    print("1. Elevar un número a una potencia dada.")
    print("2. Sumatoria.")
    print("3. Determinar si un número es primo o no.")
    print("4. Sumar dígitos múltiplos.")
    print("5. Calcular el término n-ésimo de la sucesión de Fibonacci.")
    print("6. Número perfecto")
    print("7. Máximo común divisor.")
    print("8. Mínimo común múltiplo.")
    print("0. Terminar")
    print("*********************************")
    n = m = mult = exp = opcion = 0
    opcion = int(input("Seleccione la operación a realizar: "))
    while True:
        try:
            if opcion >= 0 and opcion <= 8:
                if opcion == 1:
                    opcionelevarNumero(n, exp)
                elif opcion == 2:
                    opcionobtenerSumatoria(n)
                elif opcion == 3:
                    opcionoesNumeroPrimo(n)
                elif opcion == 4:
                    opcionsumarMultilpos(n, mult)
                elif opcion == 5:
                    opcionobtenerFibonacci(n)
                elif opcion == 6:
                    opcionesPerfecto(n)
                elif opcion == 7:
                    opcionobtenerMCD(n, m)
                elif opcion == 8:
                    opcionobtenerMCM(n, m)
                elif opcion==0:
                    return print("Menú cerrado.")
            else:
                print("Opción inválida.")
                return menu()
        except:
            print("Los valores deben ser números enteros.")
            return menu()
# principal
menu()