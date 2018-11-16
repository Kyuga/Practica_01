#Pràctica 7 - Ejercicio 03 - Llorenç Leiva
"""
Escribe  un  programa  que  lea  una  frase,  y  la  pase  como  parámetro  a  un  procedimiento,
y  éste debe mostrar la frase con un carácter en cada línea.
"""

def frase(a):
    for i in a:
        print(i)

a = input("Introduce una frase: ")

frase(a)
