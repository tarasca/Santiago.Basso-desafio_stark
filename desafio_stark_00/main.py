from data import lista_heroes
from functions import *
import os

while True:
    opt = menu()
    local_array = lista_heroes 
    
    match(opt):
        case "1":
            print_predata(lista_heroes)
            pass 
        case "2":
            print_nombres(local_array)
            pass    
        case "3":
            print_nombresYaltura(local_array)
            pass   
        case "4":
            print_masAlto(local_array)
            pass     
        case "5":
            print_masBajo(local_array)
            pass   
        case "6":
            print_avgAltura(local_array)
            pass     
        case "7":
            print_indicadores(local_array)
            pass   
        case "8":
            print_pesadez(local_array)
            pass     
        case "9":
            break   
            

        
