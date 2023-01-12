import random
import string

from palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual
#obtener una palabra cualquiera
#de la lista de palabras validas

def obtener_palabra_valida(palabras):
    palabra=random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra=random.choice(palabras)

    return palabra.upper()

def el_ahorcado():

    print("=====================================")
    print(  'Bienvenidos al Juego El Ahorcado')
    print("=====================================")

    palabra = obtener_palabra_valida(palabras)
    letras_por_adivinar=set(palabra)
    letras_adivinadas=set()
    abcdario=set(string.ascii_uppercase)

    vida=7

    while len(letras_por_adivinar) > 0 and vida > 0:
        print(f"Te quedan {vida} vidas y has adivinado estas letras: {' '.join(letras_adivinadas)}")
        palabra_lista=[letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vida])
        print (f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input ("Escoge una letra: ").upper()

        if letra_usuario in abcdario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(' ')
            else:
                vida-=1
                print(f"\nTu letra, {letra_usuario} no está en la palabra")
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva." )

        else:
            print("\nEsta letra o caracter no es válido.")

    if vida == 0:
        print(vidas_diccionario_visual[vida])
        print(f"Ahorcado,you lost. I'm sorry. Word was: {palabra}")

    else:
        print(f"Congrats, you win. Word is {palabra}!")

el_ahorcado()