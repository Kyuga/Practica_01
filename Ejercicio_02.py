#Pràctica 7 - Ejercicio 02 - Llorenç Leiva
"""
Escribe  un  programa que  lea  el  nombre  y  los  dos  apellidos  de  una  persona
(en tres  cadenas  de caracteres  diferentes),  los  pase  como  parámetros  a una
función,  y  ésta  debe  unirlos  y  devolver una única cadena. La cadena final la
imprimirá el programa por pantalla.
"""
a=input("Escribe tú primer nombre: ")
b=input("Escribe tú primer apellido: ")
c=input("Escribe tú segundo apellido: ")

def nombre(z):
    print(a,""+b,""+c)
nombre(a)
    
    
