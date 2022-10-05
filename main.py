
from random import randint
import re

print("Hola, bienvenido al juego de adivinar la palabras")

print("Tu objetivo es adivinar las peliculas \n")


peliculas=["Forest Gump","El Padrino","Gladiator","Avatar","La milla verde"
,"Parasitos","Star Wars","El Señor de los Anillos","Tiburón","Doctor Strange",
"La jungla de Cristal","Alien","Matrix","Terminator"]



chance=3
op=""
res=""


pelicula=peliculas[randint(0, len(peliculas))]
print(f"Estas son las posibles peliculas {peliculas} \n")
print(f"La película tiene {len(pelicula)} letras (contando espacios)")
while(chance>0):
    op=input("Cuál es la película\n")
    if op==pelicula:
        print(f"Felicidades la acertaste \n")
        break
    else:
        chance-=1
        print(f"Fallaste, tienes {chance} intentos")
    if(chance==1):
        res=input("Quieres una pista?si/no\n")
        if res=="si":
            print(pelicula[0:3])
        elif res=="no":
            print("Así me gusta sin pistas")
        else: 
            print("Esa respuesta no me sirve, perdiste el juego")
            break

print(f"La respuesta era "+pelicula)