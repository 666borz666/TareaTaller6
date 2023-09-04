###################################################################
#Elaborado por: Alejandro Madrigal y Daniel Campos
#Fecha de creación: 01/09/2023 Hora: 9:53 am
#Última edición: 03/09/2023 Hora:
#Versión: 3.11.4
###################################################################
#1. Elevar un número a la potencia
def elevarNumero(n, exp):
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
    if n>1:
        i = 2
        contador=0
        while i<n and contador==0:
            num=n%i
            if num==0:
                contador+=1
            i+=1
        if contador==0:
            return print(True)
        else:
            return print(False)
    return ""
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
    if n<=1:
        return n
    return obtenerFibonacci(n - 1) + obtenerFibonacci(n - 2)

#6. Número perfecto
def esPerfecto(n):
    """
    """
    divisor = 1
    numPerf = 0
    while divisor != n:
        if n % divisor == 0:
            numPerf += divisor
        divisor += 1
    if numPerf == n:
        return print(True)
    else:
        return print(False)
#7. Maximo común divisor MCD
def obtenerMCD(n, m):
    """
    """
    while m:
        n, m = m, n % m
    
    print(n)
    return ""
#8. Mínimo común múltiplo MCM
def obtenerMCM(n,m):
    """
    """
    divisorMN = 2
    mcm = 1
    while n > 1 or m > 1:
        if n % divisorMN == 0 or m % divisorMN == 0:
            if n % divisorMN == 0:
                n //= divisorMN
            if m % divisorMN == 0:
                m //= divisorMN
            mcm *= divisorMN
        else:
            divisorMN += 1
    return print(mcm)

