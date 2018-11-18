#Pràctica 4 - Ejercicio 9 - Llorenç Leiva
#Escriu un programa que demani l'amplada i l'alçada d'un rectangle i ho dibuixi
#
a=int(input("Escribe la altura del rectangulo hueco: "))
b=int(input("Escribe la base del rectangulo hueco: "))

for i in range (a,a+1):
    if ((i==1) or (i==a)):
        print ("*"*b)
    if (i<a-1):
        print (("*")+((" ")*(b-2))+("*"))
        
    
        
        

