import os



def menu()->str:
    os.system("cls")
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
    os.system("pause")

def print_heroesMasculinos(heroes:list):
    print(f"|{'nombre':^20s}|{'identidad':^30s}|{'empresa':^20s}|{'altura':^8s}|{'peso':^8s}|{'genero':^6s}|{'color ojos':^23s}|{'color pelo':^20s}|{'fuerza':^10s}|{'inteligencia':^15s}|")
    print("|--------------------|------------------------------|--------------------|--------|--------|------|-----------------------|--------------------|----------|---------------|")
    for hero in heroes:
        if(hero['genero'] == 'M'):
            print_heroe(hero)
    os.system("pause")

def print_heroesFemeninos(heroes:list):
    print(f"|{'nombre':^20s}|{'identidad':^30s}|{'empresa':^20s}|{'altura':^8s}|{'peso':^8s}|{'genero':^6s}|{'color ojos':^23s}|{'color pelo':^20s}|{'fuerza':^10s}|{'inteligencia':^15s}|")
    print("|--------------------|------------------------------|--------------------|--------|--------|------|-----------------------|--------------------|----------|---------------|")
    for hero in heroes:
        if(hero['genero'] == 'F'):
            print_heroe(hero)
    os.system("pause")

def print_MasculinoAlto(heroes:list):
    print_heroesMasculinos(heroes)
    
