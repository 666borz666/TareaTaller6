###################################################################
#Elaborado por: Alejandro Madrigal y Daniel Campos
#Fecha de creación: 01/09/2023 Hora: 9:53 am
#Última edición: 01/09/2023 Hora:
#Versión: 3.11.4
###################################################################

#1. Elevar un número a la potencia
def elevarNúmero(n, exp):
    """
    """
    if n>=0 and exp>=0:
        res=n**exp
    return print(res)

#2. Sumatoria
def obtenerSumatoria(n):
    """
    """
    i=1
    sumatoria=0
    if n>0:
        while i<=n:
            sumatoria = sumatoria+(i**2)
            i+=1
        return print(sumatoria)
    else:
        return print("Debe ser mayor a 0")

#3. Determinar si un número es primo
def esNumeroPrimo(n):
    """
    """
    i=1
    while i<=n:
        if n%i==0:
            i+=1

    return

#4. Sumar digitos múltiplos
def sumarMultiplos (n, mult):
    """
    """
    res=0
    num=0
    while n>0:
        num=n%10
        if num%mult==0:
            res+=num
        n//=10
    return print(res)

#5. Fibonacci

def obtenerFibonacci(n):
    """
    """
    res=0
    whi n >= 1:
        while n>=0:
            res=(n-1)+(n-2)
    elif n==0:
        return print(res)



    return
#Programa principal
n=int(input("n: "))
mult=int(input("mult: "))
sumarMultiplos (n, mult)