import os
from functools import reduce


def menu()->str:
    os.system("cls")
    print("<---Menu Principal Stark s.a.--->")
    print("1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print("3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("5. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    print("6. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    print("7. Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    print("8. Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    print("9. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
    print("10. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("11. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("12. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    print("13. Listar todos los superhéroes agrupados por color de ojos.")
    print("14. Listar todos los superhéroes agrupados por color de pelo.")
    print("15. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("16. Salir")
    opt = input("ingrese opcion: ")
    return opt

def print_heroe_(heroe:dict):
    print(f"nombre : {heroe['nombre']}")
    print(f"identidad : {heroe['identidad']}")
    print(f"empresa : {heroe['empresa']}")
    print(f"altura : {heroe['altura']}")
    print(f"peso : {heroe['peso']}")
    print(f"genero : {heroe['genero']}")
    print(f"color ojos : {heroe['color_ojos']}")
    print(f"color pelo : {heroe['color_pelo']}")
    print(f"fuerza : {heroe['fuerza']}")
    print(f"inteligencia : {heroe['inteligencia']}")

def print_heroe(heroe:dict):
    print(f"|{heroe['nombre']:^20s}|{heroe['identidad']:^30s}|{heroe['empresa']:^20s}|{float(heroe['altura']):^08.03f}|{float(heroe['peso']):^08.03f}|{heroe['genero']:^6s}|{heroe['color_ojos']:^23s}|{heroe['color_pelo']:^20s}|{heroe['fuerza']:^10s}|{heroe['inteligencia']:^15s}|")

def print_all(heroes:list):
    print(f"|{'nombre':^20s}|{'identidad':^30s}|{'empresa':^20s}|{'altura':^8s}|{'peso':^8s}|{'genero':^6s}|{'color ojos':^23s}|{'color pelo':^20s}|{'fuerza':^10s}|{'inteligencia':^15s}|")
    print("|--------------------|------------------------------|--------------------|--------|--------|------|-----------------------|--------------------|----------|---------------|")
    for hero in heroes:
        print_heroe(hero)

def print_heroesMasculinos(heroes:list)->list:
    heroes_masculinos = list(filter(lambda h:h['genero']=='M',heroes))
    print("<---Heroes Masculinos--->")
    print_all(heroes_masculinos)
    os.system('pause')
    return heroes_masculinos

def print_heroesFemeninos(heroes:list)->list:
    heroes_femeninos = list(filter(lambda h:h['genero']=='F',heroes))
    print("<---Heroes Femeninos--->")
    print_all(heroes_femeninos)
    os.system('pause')
    return heroes_femeninos

def print_masculinoAlto(heroes:list):
    print("<--Heroes Masculinos-->")
    print("por altura asc.")
    heroes_MarculinosAltos = heroes
    tam = len(heroes_MarculinosAltos)
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(float(heroes_MarculinosAltos[i]['altura']) < float(heroes_MarculinosAltos[j]['altura'])):
                aux = heroes_MarculinosAltos[i]
                heroes_MarculinosAltos[i] = heroes_MarculinosAltos[j]
                heroes_MarculinosAltos[j] = aux        

    print(f"|{'nombre':^20s}|{'identidad':^30s}|{'empresa':^20s}|{'altura':^8s}|{'peso':^8s}|{'genero':^6s}|{'color ojos':^23s}|{'color pelo':^20s}|{'fuerza':^10s}|{'inteligencia':^15s}|")
    print("|--------------------|------------------------------|--------------------|--------|--------|------|-----------------------|--------------------|----------|---------------|")
    for h in heroes_MarculinosAltos:
        print_heroe(h)
    os.system('pause')

def print_masAlto_(heroes:list)->dict:
    heroes_copy = heroes.copy()
    tam = len(heroes_copy)
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(float(heroes_copy[i]['altura']) < float(heroes_copy[j]['altura'])):
                aux = heroes_copy[i]
                heroes_copy[i] = heroes_copy[j]
                heroes_copy[j] = aux
    for h in heroes_copy:
        print(h)
    os.system("pause")   

def print_masAlto(heroes:list)->dict:
    print("el mas alt@ es: ")
    heroe = reduce(lambda ant,act:act if float(act['altura'])>float(ant['altura']) else ant,heroes) 
    print(heroe)
    os.system('pause')
    return heroe 

def print_masBajo(heroes:list)->dict:
    print("el mas baj@ es: ")
    heroe = reduce(lambda ant,act:act if float(act['altura'])<float(ant['altura']) else ant,heroes)
    print(heroe)
    os.system('pause')
    return heroe

def print_avgAltura(heroes:list)->float:
    print("la media de alturas es: ")
    total = 0
    for h in heroes:
        total += float(h['altura'])
    avg = total/len(heroes)
    print(f"{avg}")
    os.system('pause')
    return avg

