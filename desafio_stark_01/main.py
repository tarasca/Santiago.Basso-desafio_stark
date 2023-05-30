from data import lista_heroes
from functions import *
import os

while True:
    opt = menu().capitalize()
    local_array = lista_heroes
    

    match(opt):
        case "A":
            #Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
            local_male = print_heroesMasculinos(local_array)
            pass
        case "B":
            #Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            local_female = print_heroesFemeninos(local_array)
            pass
        case "C":
            #Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            print_masAlto(local_male)
            pass
        case "D":
            #Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            print_masAlto(local_female)
            pass
        case "E":
            #Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
            print_masBajo(local_male)
            pass
        case "F":
            #Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
            print_masBajo(local_female)
            pass
        case "G":
            #Recorrer la lista y determinar la altura promedio de los superhéroes de género M
            print_avgAltura(local_male)
            pass
        case "H":
            #Recorrer la lista y determinar la altura promedio de los superhéroes de género F
            print_avgAltura(local_female)
            pass
        case "I":
            #Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
            print_displayEtiquetas(local_array)
            pass
        case "J":
            #Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            heroes_colorOjos(local_array)
            pass
        case "K":
            #Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            heroes_colorPelo(local_array)
            pass
        case "L":
            #Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
            heroes_inteligentes(local_array)
            pass
        case "M":
            #Listar todos los superhéroes agrupados por color de ojos.
            print_colorOjos(local_array)
            pass
        case "N":
            #Listar todos los superhéroes agrupados por color de pelo.
            print_colorPelos(local_array) 
            pass
        case "O":
            #Listar todos los superhéroes agrupados por tipo de inteligencia
            print_inteligentes(local_array)
            pass
        case "P":
            #Salir
            break
        