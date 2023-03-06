print("ADIVINA EL NÚMERO")

from random import randint

intentos = 0
estimado = 0
nombre = input("Dime tu nombre: ")
numero_secreto = randint(1, 100)

print(f"Hola {nombre}, he pensado un número entre 1 y 100\ntenes 8 intentos para adivinar")


while intentos < 8:
    estimado = int(input("Cuál crees que es el número: "))
    intentos += 1 
        
    if estimado not in range (1, 101):
        print("Elegiste un número fuera de rango, elige otro por favor")
    elif estimado < numero_secreto:
        print("Elije un número mayor")
        
    elif estimado > numero_secreto:
        print("Elije un número menor")

    else:
        print(f"Felicitaciones {nombre}, adivinaste el número en {intentos} intentos!!!")
        break

if estimado != numero_secreto:
    print(f"Lo siento {nombre} se te acabaron los intentos, el número secreto era {numero_secreto}")
