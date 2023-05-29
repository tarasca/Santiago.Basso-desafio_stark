from data import lista_heroes
from functions import *
import os

while True:
    opt = menu()
    local_array = lista_heroes
    

    match(opt):
        case "1":
            #Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
            local_male = print_heroesMasculinos(local_array)
            pass
        case "2":
            #Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            local_female = print_heroesFemeninos(local_array)
            pass
        case "3":
            #Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            print_masAlto(local_male)
            pass
        case "4":
            #Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            print_masAlto(local_female)
            pass
        case "5":
            #Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
            print_masBajo(local_male)
            pass
        case "6":
            #Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
            print_masBajo(local_female)
            pass
        case "7":
            #Recorrer la lista y determinar la altura promedio de los superhéroes de género M
            print_avgAltura(local_male)
            pass
        case "8":
            #Recorrer la lista y determinar la altura promedio de los superhéroes de género F
            print_avgAltura(local_female)
            pass
        case "9":
            #Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
            pass
        case "10":
            #Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            pass
        case "11":
            #Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            pass
        case "12":
            #Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
            pass
        case "13":
            #Listar todos los superhéroes agrupados por color de ojos.
            pass
        case "14":
            #Listar todos los superhéroes agrupados por color de pelo.
            pass
        case "15":
            #Listar todos los superhéroes agrupados por tipo de inteligencia
            pass
        case "16":
            #Salir
            break
        