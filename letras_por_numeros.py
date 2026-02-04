"""
Docstring for letras_por_numeros
Reemplazar las letras de un string por su index en el alfabeto (e.g. A = 1 , B = 2 , C = 3 ...)

Consideraciones Adicionales:
Ignorar espacios.
Hacer clean up del string antes de comenzar el swap (para eliminar acentos y caracteres especiales, se sugiere meter en este proceso de clean up 
el ignorado de espacios).
Ejemplo:

func("abc def"); // returns '1 2 3 4 5 6';

"""
import re
from unidecode import unidecode

def letras_por_numeros(palabra):

    palabra_procesada = cleanup(palabra=palabra)

    diccionario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    numeros = ''
    for letra in palabra_procesada.lower():

        if letra in diccionario:
            numeros += " "+ str (diccionario.index(letra)+1)
            
    print(numeros)
 

def cleanup(palabra):
    palabra_partes = palabra.split()
    palabra_sin_espacios = ''.join(palabra_partes)

    parts = re.split(r'([ñÑ])', palabra_sin_espacios)

    palabra_sin_tildes = ''.join([(unidecode(x) if x != 'ñ' and x != 'Ñ' else x) for x in parts])
    
    palabra_sin_caracteres_especiales = limpio = re.sub(r'[^a-zA-Z0-9\sñÑ]', '', palabra_sin_tildes)

    return palabra_sin_caracteres_especiales


if __name__ == "__main__":
    resultado = letras_por_numeros("ábc def@Ñ")
