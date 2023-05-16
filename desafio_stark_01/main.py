from data import lista_heroes
from functions import *
import os

while True:
    opt = menu()
    local_array = lista_heroes

    match(opt):
        case "1":
            print_heroesMasculinos(local_array)
            pass
        case "2":
            print_heroesFemeninos(local_array)
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            pass
        case "13":
            pass
        case "14":
            pass
        case "15":
            pass
        case "16":
            break
        