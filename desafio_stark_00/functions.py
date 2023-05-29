import os
import re
from functools import reduce


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
    local = heroes
    tam = len(heroes)
    print("comparando...")
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(float(local[i]['altura']) > float(local[j]['altura'])):
                pass
            else:
                aux = local[i]
                local[i]=local[j]
                local[j]=aux
    alto = local[0]
    print("listado de super-nombres y super_alturas(mayor a menor)")
    print_all(local)
    os.system("pause")
    return alto

def print_masBajo(heroes:list)->dict:
    local = heroes
    tam = len(heroes)
    print("comparando...")
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(float(local[i]['altura']) < float(local[j]['altura'])):
                pass
            else:
                aux = local[i]
                local[i]=local[j]
                local[j]=aux
    bajo = local[0]
    print("listado de super-nombres y super_alturas(menor a mayor)")
    print_all(local)
    os.system("pause")
    return bajo
    
def print_avgAltura(heroes:list):
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
    alto = print_masAlto(heroes)
    bajo = print_masBajo(heroes)
    
    print(f"Min: {bajo['nombre']}")
    print(f"max: {alto['nombre']}")

def print_pesadez(heroes:list):
    local = heroes
    tam = len(heroes)
    print("comparando...")
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(float(local[i]['peso']) > float(local[j]['peso'])):
                pass
            else:
                aux = local[i]
                local[i]=local[j]
                local[j]=aux

    print("listado de super-nombres y super-pesos(mayor a menor)")
    print_all(local)
    os.system("pause")

    local = heroes
    tam = len(heroes)
    print("comparando...")
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(float(local[i]['peso']) < float(local[j]['peso'])):
                pass
            else:
                aux = local[i]
                local[i]=local[j]
                local[j]=aux

    print("listado de super-nombres y super-pesos(menor a mayor)")
    print_all(local)
    os.system("pause")

