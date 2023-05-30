import os
from functools import reduce


def menu()->str:
    os.system("cls")
    print("<---Menu Principal Stark s.a.--->")
    print("A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    print("B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print("C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    print("F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    print("G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    print("H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    print("I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores")#(ítems C a F)
    print("J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("L. Determinar cuántos superhéroes tienen cada tipo de inteligencia.")#(En caso de no tener, Inicializarlo con ‘No Tiene’)
    print("M. Listar todos los superhéroes agrupados por color de ojos.")
    print("N. Listar todos los superhéroes agrupados por color de pelo.")
    print("O. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("P. Salir")
    opt = input("ingrese opcion: ")
    return opt
def divisor_line():
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
def cabezal_print():
    print(f"|{'nombre':^20s}|{'identidad':^30s}|{'empresa':^20s}|{'altura':^8s}|{'peso':^8s}|{'genero':^6s}|{'color ojos':^23s}|{'color pelo':^20s}|{'fuerza':^10s}|{'inteligencia':^15s}|")
    print("|--------------------|------------------------------|--------------------|--------|--------|------|-----------------------|--------------------|----------|---------------|")

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
    cabezal_print()
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

    cabezal_print()
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
    print_heroe_(heroe)
    os.system('pause')
    return heroe 

def print_masBajo(heroes:list)->dict:
    print("el mas baj@ es: ")
    heroe = reduce(lambda ant,act:act if float(act['altura'])<float(ant['altura']) else ant,heroes)
    print_heroe_(heroe)
    os.system('pause')
    return heroe

def print_avgAltura(heroes:list)->float:
    print("")
    total = 0
    for h in heroes:
        total += float(h['altura'])
    avg = total/len(heroes)
    print(f"la media de alturas es: {avg}m")
    os.system('pause')
    return avg

def print_displayEtiquetas(heroes:list):
    loop = True
    while loop:
        os.system('cls')
        print("---[Heroes por etiquetas]---")
        print("1- heroe m alto")
        print("2- heroe f alta")
        print("3- heroe m bajo")
        print("4- heroes f bajo")
        print("5- salir")
        res = input("ingresar opcion(num): ")
        while(not res.isnumeric() or int(res)>5):
            res = input("ERROR!!!reingresar opcion: ")
        match(res):
            case "1":
                hm = list(filter(lambda h:h['genero']=='M',heroes))
                print_masAlto(hm)
                pass
            case "2":
                hf = list(filter(lambda h:h['genero']=='F',heroes))
                print_masAlto(hf)
                pass
            case "3":
                hm = list(filter(lambda h:h['genero']=='M',heroes))
                print_masBajo(hm)
                pass
            case "4":
                hf = list(filter(lambda h:h['genero']=='F',heroes))
                print_masBajo(hf)
                pass
            case "5":
                break

def heroes_colorOjos(heroes:list):
    h_copy = heroes.copy()
    _colores = []
    for h in h_copy:
        _colores.append(h['color_ojos'])
    set_colores = set(_colores)
    x = 0
    for color in set_colores:
        for h in h_copy:
            if h['color_ojos'] == color:
                x+=1
        print(f"{color}: {x}")
    os.system('pause')
    
def heroes_colorPelo(heroes:list):
    h_copy = heroes.copy()
    _pelos = []
    for h in h_copy:
        _pelos.append(h['color_pelo'])
    set_pelos = set(_pelos)
    x = 0
    for pelo in set_pelos :
        for h in h_copy:
            if h['color_pelo'] == pelo:
                x+=1
        print(f"{pelo}: {x}")
    os.system('pause')

def heroes_inteligentes(heroes:list):
    h_copy = heroes.copy()
    _int = []
    for h in h_copy:
        if h['inteligencia'] == "":
            h['intelgiencia'] = 'no tiene'
        _int.append(h['inteligencia'])
    set_int = set(_int)
    x = 0
    for inte in set_int:
        for h in h_copy:
            if h['inteligencia'] == inte:
                x+=1
        print(f"{inte}: {x}")
    os.system('pause')

def print_colorOjos(heroes:list):
    print("--Heroes x color de ojos-->")
    h_copy = heroes.copy()
    _colores = []
    for h in h_copy:
        _colores.append(h['color_ojos'])
    set_colores = set(_colores)
    
    for color in set_colores:
        print(f"color de ojos: {color}")
        cabezal_print()
        for h in h_copy:
            if(h['color_ojos'] == color):
                print_heroe(h)
        divisor_line()    
    os.system('pause')

def print_colorPelos(heroes:list):
    print("--Heroes x color de pelo-->")
    h_copy = heroes.copy()
    _pelos = []
    for h in h_copy:
        _pelos.append(h['color_pelo'])
    set_pelos = set(_pelos)
    
    for pelo in set_pelos:
        if(pelo == ""):
            pelo = 'no tiene'
        print(f"color de pelo: {pelo}")
        cabezal_print()
        for h in h_copy:
            if(h['color_pelo'] == pelo):
                print_heroe(h)
        divisor_line()    
    os.system('pause')

def print_inteligentes(heroes:list):
    print("--Heroes x inteligencia-->")
    h_copy = heroes.copy()
    _tipos = []
    for h in h_copy:
        if(h['inteligencia'] == ""):
            h['inteligencia'] = "no tiene"
        _tipos.append(h['inteligencia'])
    tipos_intlgc = set(_tipos)

    for intlgc in tipos_intlgc:
        
        print(f"inteligencia: {intlgc}")
        cabezal_print()
        for h in h_copy:
            if(h['inteligencia'] == intlgc):
                print_heroe(h)
        divisor_line()
    os.system('pause')
        