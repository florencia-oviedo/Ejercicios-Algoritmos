'''
Docstring for isograma
Un isograma es una palabra que no tiene letras repetidas. Consideraciones Adicionales:

Un string vacío es un isograma.
La función tiene que ser case insensitive e ignorar acentos.
Si el string tiene mas de una palabra retornar false.
Se tiene que hacer clean up del string antes de comparar.

func("Murciélago"); // returns true
func("reto"); // returns false
func("Casa"); // returns false
func("PeRrO"); // returns false
func("GaTo"); // returns true
'''

import re
from unidecode import unidecode

def is_isograma(palabra):

    if not palabra :
        return True
    
    palabra_partes = palabra.split() 
    if len(palabra_partes) > 1 :
        return False

    is_isograma = True
    lista_aux = []
    parts = re.split(r'([ñÑ])', palabra)
    palabra_sin_tildes = ''.join([(unidecode(x) if x != 'ñ' and x != 'Ñ' else x) for x in parts])
 
    for letra in palabra_sin_tildes.lower():

        if letra in lista_aux:
            is_isograma = False
            break
        
        else:
            lista_aux.append(letra)
  
    return is_isograma

if __name__ == "__main__":

    boolean = is_isograma("Murciélago")

    print("resultado: ",boolean)
