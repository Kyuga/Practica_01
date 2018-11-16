#Pràctica 7 - Ejercicio 01 - Llorenç Leiva
""""
Escribe un programa que pida un texto por pantalla,este texto lo pase como
parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.
"""
a=input("Escribe un texto: ")
b=input("Escribe otra frase: ")#Pongo una segunda variable para demostrar que
#solo pone en minus y mayus el primer input.

def texto(x):
    print (x.upper())
    print (x.lower())
texto(a)
    
