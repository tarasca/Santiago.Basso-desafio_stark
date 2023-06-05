from data import lista_heroes
from functions import *
import os

MAX = 'maximo'
MIN = 'minimo'

while True:
    opt = menu()
    local_array = lista_heroes 
    
    match(opt):
        case "0":
            test_thing(local_array)
            pass
        case "1":
            stark_normalizar_datos(local_array)
            pass 
        case "2":
            stark_imprimir_nombre_heroes(local_array)
            pass    
        case "3":
            stark_imprimir_nombres_y_alturas(local_array)
            pass   
        case "4":
            stark_calcular_imprimir_heroe(local_array,MAX,'altura')
            pass     
        case "5":
            stark_calcular_imprimir_heroe(local_array,MIN,'altura')
            pass   
        case "6":
            print_avgAltura(local_array)
            pass     
        case "7":
            print_indicadores(local_array)
            pass   
        case "8":
            stark_calcular_imprimir_heroe(local_array,MAX,'peso')
            stark_calcular_imprimir_heroe(local_array,MIN,'peso')
            pass     
        case "9":
            break   
            

        
