import os
import re
from functools import reduce

admin = True

set = ()

def menu():
    os.system("cls")
    print("*****STARK INDUSTRIES*****")
    print("<---Menu Principal--->")
    if(admin):
        print("0. TESTEOS")
    print("1. Analizar detenidamente el set de datos")
    print("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    print("3. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    print("4. Recorrer la lista y determinar cuál es el superhéroe más alto")
    print("5. Recorrer la lista y determinar cuál es el superhéroe más bajo")
    print("6. Recorrer la lista y determinar la altura promedio de los superhéroes")
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

def print_predata(heroes:list):
    print("set de super-datos: ")
    print_all(heroes)
    os.system('pause')

def print_nombres(heroes:list):
    print("listado de super-nombres")
    for heroe in heroes:
        print(f"|{heroe['nombre']:^20s}|")
    os.system("pause")

def print_nombresYaltura(heroes:list):
    print("listado de super-nombres y super_alturas")
    for heroe in heroes:
        print(f"|{heroe['nombre']:^20s}|{float(heroe['altura']):^08.03f}|")
    os.system("pause")

def print_masAlto(heroes:list)->dict:
    alto = reduce(lambda ant,act:act if float(ant['altura'])<float(act['altura']) else ant,heroes)
    print(f"el heroe mas alto es:")
    print_heroe_(alto)
    os.system('pause')
    return alto

def print_masBajo(heroes:list)->dict:
    bajo = reduce(lambda ant,act:act if float(ant['altura'])>float(act['altura']) else ant,heroes)
    print(f"el heroe mas alto es:")
    print_heroe_(bajo)
    os.system('pause')
    return bajo
    
def print_avgAltura(heroes:list)->float:
    tam = len(heroes)
    acum = 0
    for h in heroes:
        acum += float(h["altura"])
    avg = acum / tam
    print(f"la media de super alturas es: {avg}")
    os.system('pause')
    return avg

def print_indicadores(heroes:list):
    alto = reduce(lambda ant,act:act if float(ant['altura'])<float(act['altura']) else ant,heroes)
    bajo = reduce(lambda ant,act:act if float(ant['altura'])>float(act['altura']) else ant,heroes)

    print("Maximo:")
    print_heroe_(alto)
    print("\nMinimo:")
    print_heroe_(bajo)
    os.system('pause')

def print_pesadez(heroes:list):
    pesuti = reduce(lambda ant,act:act if float(ant['peso'])<float(act['peso']) else ant,heroes)
    plumita = reduce(lambda ant,act:act if float(ant['peso'])>float(act['peso']) else ant,heroes)
    
    print("el mas pesado es:")
    print_heroe_(pesuti)
    print("\nel menos pesado es:")
    print_heroe_(plumita)
    os.system('pause')

#---------------------------------------------------------------------------------------------------------------------------

#imprime el titular de un submenu utilizado para testear funciones, ya q su uso es interno no hay muchas validaciones
def titular_testing()->str:
    print("---testing functions---")
    print("0. Salir")
    print("1. stark_normalizar_datos")
    print("2. obtener_nombre")
    print("3. imprimir_dato")
    print("4. stark_imprimir_nombres")
    print("5. obtener_nombre_y_dato")
    print("6. stark_imprimir_nombres_alturas")
    print("7. calcular_max")
    print("8. calcular_min")
    print("9. calcular_max_min_dato")
    print("10. stark_calcular_imprimir_heroes")
    print("11 sumar_dato_heroe")
    print("12 dividir")
    print("13 calcular_promedio")
    print("14 stark_calcular_imprimir_promedio_altura")
    print("15 imprimir_menu")
    print("16 validar_entero")
    print("17 stark_menu_principal")
    print("18 stark_marvel_app")
    opt = input("ingrese opcion: ")
    return opt

def test_thing(heroes:list):
    #funcion para testeo de funciones, cuenta con menu or match
    #la idea es usar cada case para testear con diferentes valores cada funciony corroborar su funcionamiento
    loop = True
    while loop:
        os.system('cls')
        opt = titular_testing()
        match(opt):
            case "1":
                stark_normalizar_datos(heroes)
                pass
            case "2":
                print(obtener_nombre(heroes[0]))
                pass
            case "3":
                msg = input("que mensaje desea imprimir?:")
                imprimir_dato(msg)
                pass
            case "4":
                print("Nombre de heroes con texto formateado")
                stark_imprimir_nombre_heroes(heroes)
                pass
            case "5":
                dato = input("ingrese dato que desea: ")
                print(obtener_nombre_y_dato(heroes[0],dato))
                pass
            case "6":
                print("nombres y alturas de heroes")
                stark_imprimir_nombres_y_alturas(heroes)
                pass
            case "7":
                atr7 = input("calcular maximo\n ingresar atributo numerico(altura,peso o fuerza): ")
                print(calcular_max(heroes,atr7))
                pass
            case "8":
                atr8 = input("calcular minimo\n ingresar atributo numerico(altura,peso o fuerza): ")
                print(calcular_min(heroes,atr8))
                pass
            case "9":
                tipo9 = input("maximo o minimo?")
                atr9 = input(f"calcular {tipo9}, ingrese atributo numerico(altura,peso o fuerza): ")
                print(calcular_max_min_dato(heroes,tipo9,atr9))
                pass
            case "10":
                tipo10 = input("maximo o minimo?")
                atr10 = input(f"calcular {tipo10}, ingrese atributo numerico(altura,peso o fuerza): ")
                stark_calcular_imprimir_heroe(heroes,tipo10,atr10)
                pass
            case "11":
                atr11 = input("acumular dato, ingrese atributo numerico(altura,peso o fuerza): ")
                sumar_dato_heroe(heroes,atr11)
                pass
            case "12":
                numerador = int(input("ingrese divisor: "))
                denominador = int(input("ingrese dividendo: "))
                print(dividir(numerador,denominador))
                pass
            case "13":
                calcular_promedio(heroes,)
                pass
            case "14":
                pass
            case "15":
                pass
            case "16":
                pass
            case "17":
                pass
            case "18":
                pass
            case "0":
                break
        os.system('pause')



def stark_normalizar_datos(heroes:list):
    #con una bandera compruebo que cada dato sea del tipo especifico, caso contrario casteo
    flag = False
    if(len(heroes) > 0):
        for h in heroes:
            if((type(h['nombre']) != str) or (type(h['identidad']) != str) or 
               (type(h['empresa']) != str) or (type(h['altura']) != float) or 
               (type(h['peso']) != float) or (type(h['genero']) != str) or 
                (type(h['color_ojos']) != str) or (type(h['color_pelo']) != str) or 
                (type(h['fuerza']) != int) or (type(h['inteligencia']) != str)):
                h['nombre'] = str(h['nombre'])
                h['identidad'] = str(h['identidad'])
                h['empresa'] = str(h['empresa'])
                h['genero'] = str(h['genero'])
                h['color_ojos'] = str(h['color_ojos'])
                h['color_pelo'] = str(h['color_pelo'])
                h['inteligencia'] = str(h['inteligencia'])

                h['altura'] = float(h['altura'])
                h['peso'] = float(h['peso'])

                h['fuerza'] = int(h['fuerza'])
                flag = True
    if(flag == True):
        print("Datos normalizados.")
        
def obtener_nombre(h:dict)->str:
    nombre_format = "Nombre: " + h['nombre']
    return nombre_format
    
def imprimir_dato(string:str):
    print(string)

def stark_imprimir_nombre_heroes(heroes:list)->int:
    ok = -1
    if(len(heroes)>0):
        for h in heroes:
            imprimir_dato(obtener_nombre(h))
            ok = 0
    return ok

def obtener_nombre_y_dato(h:dict, h_key:str):
    #forma automata de conseguir un dato formateado si este existe,caso contrario devuelve -1
    ok = -1
    all_keys = h.keys()
    if(h_key in all_keys):
        key_value = h.get(h_key)
        return obtener_nombre(h) + " | "+ h_key + ": " + str(key_value)
    else:
        return ok
    
def stark_imprimir_nombres_y_alturas(heroes:list):
    for h in heroes:
        print(obtener_nombre_y_dato(h,'altura'))
    
def calcular_max(heroes:list,h_key:str)->dict:
    #compruebo que las keys sean correctas, caso contrario devuelve -1
    keys = ['altura','peso','fuerza']
    if(h_key in keys):
        maximo = reduce(lambda h1,h2:h1 if h1[h_key] > h2[h_key] else h2,heroes)
        return maximo
    else: 
        return -1

def calcular_min(heroes:list,h_key:str)->dict:
    #compruebo que las keys sean correctas, caso contrario devuelve -1
    keys = ['altura','peso','fuerza']
    if(h_key in keys):
        minimo = reduce(lambda h1,h2:h1 if h1[h_key] < h2[h_key] else h2,heroes)
        return minimo
    else:
        return -1

def calcular_max_min_dato(heroes:list,type:str,h_key:str)->dict:
    #corroboro el 2do parametro,caso positivo obtengo maximo o minimo, caso negativo devuelve -1
    if(type == 'maximo'):
        return calcular_max(heroes,h_key)
    elif(type == 'minimo'):
        return calcular_min(heroes,h_key)
    else:
        print("error!!! ingresar 'maximo' o 'minimo'.")
        os.system('pause')
        return -1

def stark_calcular_imprimir_heroe(heroes:list,type:str,h_key:str):
    list_opt = ['maximo','minimo']
    if(len(heroes)>0 and type in list_opt):
        print(f"{type} {h_key}: {calcular_max_min_dato(heroes,type,h_key)}")
    else:
        return -1

#mal funcionamiento, me tira error el reduce, dice que el segundo parametro no es 'subscriptable' 
def sumar_dato_heroe(heroes:list, h_key:str)->dict:
    for h in heroes:
        if(not h):
            return -1
        else:
            pass
    
    acum = reduce(lambda act,ant:act[h_key] + ant[h_key],heroes)
    return acum

def dividir(num,den):
    #corroboro no dividir por 0
    if(den == 0):
        return 0
    else :
        return num/den

def calcular_promedio(heroes:list,h_key:str):
    #mal funcionamiento debido a error acarriado en funcion sumar_dato_heroe
    return dividir(sumar_dato_heroe(heroes,h_key),len(heroes))

def imprimir_promedio_altura(heroes:list):
    #mal funcionamiento debido a error acarriado en funcion sumar_dato_heroe
    if(len(heroes)>0):
        imprimir_dato(calcular_promedio(heroes,'altura'))
    else:
        return -1
    
def imprimir_menu():
    #limpia pantalla e imprime el menu
    os.system("cls")
    imprimir_dato("*****STARK INDUSTRIES*****")
    imprimir_dato("<---Menu Principal--->")
    if(admin):
        print("0. TESTEOS")
    imprimir_dato("1. Analizar detenidamente el set de datos")
    imprimir_dato("2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    imprimir_dato("3. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    imprimir_dato("4. Recorrer la lista y determinar cuál es el superhéroe más alto")
    imprimir_dato("5. Recorrer la lista y determinar cuál es el superhéroe más bajo")
    imprimir_dato("6. Recorrer la lista y determinar la altura promedio de los superhéroes")
    imprimir_dato("7. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    imprimir_dato("8. Calcular e informar cual es el superhéroe más y menos pesado.")
    imprimir_dato("9. salir")

def validar_entero(cad:str):
    #valida q sea digito una cadena
    #return cad.isdigit()
    if(cad.isdigit()):
        return True
    else:
        return False
    
def menu_principal()->int:
    #funcion menu, imprime y devuelve la opcion a ejecutar
    imprimir_menu()
    opt = input("ingrese opcion(numero): ")
    if(validar_entero(opt)):
        return int(opt)
    else:
        return -1
    
def stark_marvel_app(heroes:list):
    #funcion madre, aca sucede toda la magia :$
    while True:
        match(menu_principal()):
            case 1:
                stark_normalizar_datos(heroes)
                pass
            case 2:
                stark_imprimir_nombre_heroes(heroes)
                pass
            case 3:
                stark_imprimir_nombres_y_alturas(heroes)
                pass
            case 4:
                stark_calcular_imprimir_heroe(heroes,'maximo','altura')
                pass
            case 5:
                stark_calcular_imprimir_heroe(heroes,'minimo','altura')
                pass
            case 6:
                #defectuosa
                imprimir_promedio_altura(heroes)
                pass
            case 7:
                stark_calcular_imprimir_heroe(heroes,'maximo','altura')
                stark_calcular_imprimir_heroe(heroes,'minimo','altura')
                pass
            case 8:
                stark_calcular_imprimir_heroe(heroes,'maximo','peso')
                stark_calcular_imprimir_heroe(heroes,'minimo','peso')
                pass
            case 9:
                exit = input("desea salir?(y/n): ")
                t = ['y','n']
                while(exit not in t):
                    exit = input("opcion no valida, reignresar: ")
                if(exit == 'y'):
                    print("STARK_APP CERRANDOSE...")
                    break
                elif(exit  == 'n'):
                    print("volviendo al sistema...")
                    pass
            case error:
                print("error!!! opcion no valida reingresar...")
        os.system('pause')