import os
import re


def menu():
    os.system("cls")
    print("*****STARK INDUSTRIES*****")
    print("<---Menu Principal--->")
    print("1. Analizar detenidamente el set de datos")
    print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    print("3. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)")
    print("5. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)")
    print("6. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
    print("7. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("8. Calcular e informar cual es el superhéroe más y menos pesado.")
    print("9. salir")
    opt = input("ingrese opcion(numero): ")
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
    os.system("pause")

def print_predata(heroes:list):
    print("set de super-datos: ")
    print_all(heroes)

def print_nombres(heroes:list):
    print("listado de super-nombres: \n")
    for heroe in heroes:
        print(f"|{heroe['nombre']:^20s}|")
    os.system("pause")

def print_nombresYaltura(heroes:list):
    print("listado de super-nombres y super_alturas")
    for heroe in heroes:
        print(f"|{heroe['nombre']:^20s}|{float(heroe['altura']):^08.03f}|")
    os.system("pause")

def print_masAlto(heroes:list)->dict:
    print("listado de super-nombres y super_alturas")
    for heroe in heroes:
        print(f"|{heroe['nombre']:^20s}|{float(heroe['altura']):^08.03f}|")
    print("____________________________________________________________________________")
    tam = len(heroes)
    print("comparando...")
    for i in range(0, tam-1):
        for j in range(1,tam):
            mas_alto = heroes[i]
            if(float(heroes[j]['altura']) > float(mas_alto['altura'])):
                mas_alto = heroes[j]
            else:
                pass

    print("el mas alto es:")
    print_heroe_(mas_alto)
    os.system("pause")
    return mas_alto

def print_masBajo(heroes:list)->dict:
    print("listado de super-nombres y super_alturas")
    for heroe in heroes:
        print(f"|{heroe['nombre']:^20s}|{float(heroe['altura']):^08.03f}|")
    print("____________________________________________________________________________")
    tam = len(heroes)
    print("comparando...\n")
    for i in range(0, tam-1):
        for j in range(1,tam):
            mas_bajo = heroes[i]
            if(float(heroes[j]['altura']) < float(mas_bajo['altura'])):
                mas_bajo = heroes[j]
            else:
                pass

    print("el mas bajo es:")
    print_heroe_(mas_bajo)

    os.system("pause")
    return mas_bajo
    
def print_avgAltura(heroes:list):
    print("listado de super-nombres y super_alturas")
    for heroe in heroes:
        print(f"|{heroe['nombre']:^20s}|{float(heroe['altura']):^08.03f}|")
    print("____________________________________________________________________________")

    alturas = []
    for heroe in heroes:
        alturas.append(float(heroe['altura']))
    tam = len(alturas)
    acum = 0
    for i in range(tam):
        acum = acum+alturas[i]
    avg = acum/tam

    print(f"la media de alturas es: {avg}m")
    os.system("pause")

def print_indicadores(heroes:list):
    print(f"Min: {print_masBajo(heroes)['nombre']}")
    print(f"max: {print_masAlto(heroes)['nombre']}")

def print_pesadez(heroes:list):
    print("super-lista con sus super-pesos")
    for heroe in heroes:
        print(f"|{heroe['nombre']:^20s}|{float(heroe['peso']):^08.03f}|")
    print("balanceando...")
    tam = len(heroes)
    for i in range(0,tam-1):
        for j in range(1,tam):
            if(heroes[i]['peso'] > heroes[j]['peso']):
                mas_pesado = heroes[i]
                menos_pesado = heroes[j]
            elif(heroes[i]['peso'] < heroes[j]['peso']):
                mas_pesado = heroes[j]
                menos_pesado = heroes[i]
            else:
                pass
    print(f"mas pesado: {mas_pesado['nombre']}")
    print(f"menos pesado: {menos_pesado['nombre']}")
    os.system("pause")
