###################################################################
#Elaborado por: Alejandro Madrigal y Daniel Campos
#Fecha de creación: 02/09/2023 Hora: 5:33 pm
#Última edición: xx/xx/xxxx Hora:
#Versión: 3.11.4
###################################################################
from funciones import *
#def de funciones
#1
def elevarNumeroAux(n, exp):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n and exp, int)==False:
        return "Ambos datos deben ser enteros positivos mayores o iguales que cero."
    else: 
        opcionelevarNumero(n, exp)
    
def opcionelevarNumero(n,exp):
    """
    F: Entradas de la función elevar número
    E (int): Valor de la base y el exponente 
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Elevar un número.")
            n=int(input("Digite el valor de la base:"))
            exp=int(input("Digite el valor del exponente: "))
            return print(elevarNumeroAux(n, exp))
        except:
            return "Los valores deben ser números enteros."
#2
def obtenerSumatoriaAux(n):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int)==True:
        obtenerSumatoria(n)
        if n<0:
            return "El número debe ser mayor que 0."
    else: 
        return "Debe ingresar solamente valores numéricos."

def opcionobtenerSumatoria(n):
    """
    F: Entradas de la función obtener sumatoria
    E (int): Valor del límite que llega la sumatoria 
    S (int): Valor de la operación ya realizada
    """
    while True:
        try: 
            print("Escriba un número límite y calcula el valor de la sumatoria del número indicado y los números anteriores al cuadrado.")
            n=int(input("Digite un número límite de la sumatoria: "))
            return print(obtenerSumatoriaAux(n))
        except:
            return "Los valores deben ser números enteros."
#3
def esNumeroPrimoAux(n):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int)==True:
        esNumeroPrimo(n)
        if n<1:
            return "El número debe ser mayor que 1."
    else: 
        return "Debe ingresar solamente valores numéricos."    

def opcionoesNumeroPrimo(n):
    """
    F: Entradas de la función número primo
    E (int): Valor numérico a revisar
    S (int): Valor de la operación ya realizada
    """
    while True:
        try: 
            print("Escriba un número límite y calcula el valor de la sumatoria del número indicado y los números anteriores al cuadrado.")
            n=int(input("Digite un número: "))
            return print(esNumeroPrimoAux(n))
        except:
            return "Los valores deben ser números enteros."
#4
def sumarMultiplosAux(n, mult):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n and mult, int)==True:
        obtenerSumatoria(n)
        if n<0 or mult<0:
            return "El número debe ser mayor que 0."
    else: 
        return "Debe ingresar solamente valores numéricos."
    
def opcionsumarMultilpos(n, mult):
    """
    F: Entradas de la función sumar múltiplos
    E (int): Valor de la base y el exponente 
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Suma de los múltiplos del dígito.")
            n=int(input("Digite un número: "))
            mult=int(input("Digite un dígito: "))
            return print(sumarMultiplosAux(n, mult))
        except:
            return "Los valores deben ser números enteros."
#5
def obtenerFibonacciAux(n):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int)==True:
        obtenerSumatoria(n)
        if n<1:
            return "El número debe ser mayor que 1."
    else: 
        return "Debe ingresar solamente valores numéricos."

def opcionobtenerFibonacci(n):
    """
    F: Entradas de la función bbtener Fibonacci
    E (int): Valor numérico a revisar
    S (int): Valor de la operación ya realizada
    """
    while True:
        try: 
            print("Obtiene la suseción de Fibonaccio del número dado.")
            n=int(input("Digite un número: "))
            return print(obtenerFibonacciAux(n))
        except:
            return "Los valores deben ser números enteros."
#6
def esPerfectoAux(n):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n, int)==False:
        return "El dígito debe ser mayor que cero."
    else: 
        opcionesPerfecto(n)
        
def opcionesPerfecto(n):
    """
    F: Entradas de la función número perfecto
    E (int): Valor de la base y el exponente 
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Número perfecto (Un número perfecto es un número natural que es igual a la suma de sus divisores propios positivos).")
            n=int(input("Digite un número:"))
            return print(elevarNumeroAux(n))
        except:
            return "El valor debe ser entero positivo."
#7
def obtenerMCDaux(n, m):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n and m, int)==False:
        return "Ambos datos deben ser enteros positivos mayores o iguales que cero."
    else: 
        opcionelevarNumero(n, m)

def opcionobtenerMCD(n,m):
    """
    F: Entradas de la función obtener el máximo común divisor
    E (int): Valor de la base y el exponente 
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Obtener el máximo común divisor.")
            n=int(input("Digite un número:"))
            m=int(input("Digite otro número: "))
            return print(elevarNumeroAux(n, m))
        except:
            return "Los valores deben ser números enteros."
#8
def obtenerMCMaux(n, m):
    """
    F: Valida que las entradas sean valores correctos
    E (int): Valores ingresados por el usuario
    S (func or string): Función ya validada o mensaje del error
    """
    if isinstance(n and m, int)==False:
        return "Ambos datos deben ser enteros positivos mayores o iguales que cero."
    else: 
        opcionelevarNumero(n, m)

def opcionobtenerMCM(n,m):
    """
    F: Entradas de la función obtener el máximo común divisor
    E (int): Valor de la base y el exponente 
    S (int): Valor de la operación ya realizada
    """
    while True:
        try:
            print("Obtener el mínimo común múltiplo.")
            n=int(input("Digite un número:"))
            m=int(input("Digite otro número: "))
            return print(elevarNumeroAux(n, m))
        except:
            return "Los valores deben ser números enteros."
    
    
#menú
def menuAux(n):
    """
    F: Valida que la entrada sea un valor correcto
    E (int): Valor ingresados por el usuario
    S (func or string): Función seleccionada o mensaje del error
    """
    if isinstance(n, int)==True:
        menu()
    else: 
        return "Debe ingresar solamente números."

def menu(n):
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
    while True: 
        try: 
            opcion=int(input("Seleccione la operación a realizar: "))
            if opcion>=0 and opcion<=8:
                if opcion==1:
                    opcionelevarNumero(n)
                elif opcion==2:
                    opcionobtenerSumatoria(n)
                elif opcion==3:
                    opcionoesNumeroPrimo(n)
                elif opcion==4:
                    opcionsumarMultilpos(n)
                elif opcion==5:
                    opcionobtenerFibonacci(n)
                elif opcion==6:
                    opcionesPerfecto(n)
                elif opcion==7:
                    opcionobtenerMCD(n)
                elif opcion==8:
                    opcionobtenerMCM(n)
                else:
                    return
            else: 
                print("Opción inválida.")
        except:
            print("\n 1. Debe ingresar números enteros únicamente. \n 2. No ingrese caracteres diferentes de números. \n")
#principal
menu(n)