import re,os



def extraer_iniciales(h_name:str):
    #verifico q no este vacio, saco los 'the' y los '-'
    h_iniciales = ""#declaro retorno
    if(len(h_name)>0):#valido lista no vacia
        if('the' in h_name):
            h_name = h_name.replace('the','')
        if('-' in h_name):
            h_name = h_name.replace('-',' ')
        for char in h_name:#itero los caracteres y si es mayuscula luego le concateno un '.'
            if(char.isupper()):
                h_iniciales = h_iniciales + char + '.'#modifico la inicial para q sea correcta
        return h_iniciales
    else:
        return 'N/A'
    
def definir_iniciales_nombre(h:dict):
    if(type(h) == dict and h['nombre']):#valido q sea dict y q su campo 'nombre' no este vacio
        h.update({'iniciales':extraer_iniciales(h['nombre'])})
        return True
    else:
        return False

def agregar_iniciales_nombre(h_list:list):
    ok = False#declaro retorno
    if(type(h_list) == list and len(h_list)>0):#verifico q sea lista y no este vacia
        for h in h_list:#defino iniciales primero
            if(definir_iniciales_nombre(h)):
                pass
            else:
                print("el origen de datos no contiene el formato correcto")
                return ok
        ok = True
        return ok
    else:
        ok

def stark_imprimir_nombres_con_iniciales(h_list:list):

    if(type(h_list)==list and len(h_list)>0):
        if(agregar_iniciales_nombre(h_list)):
            for h in h_list:
                print(f"* {h['nombre']} ({h['iniciales']})")

    
def generar_codigo_heroe(h_id:int,h_genero:str):
    g = ['M','F','NB']#lista auxiliar para validacion de generos
    if(type(h_id) == int and h_genero in g and h_genero != ''):#valido el id, que el genero exista y q no este vacio
        if(h_genero == 'M' or h_genero == 'F'):#genero dos tipos de codigo segun el largo del genero
            codigo = f"{h_genero}-{h_id:08d}"
        else:
            codigo = f"{h_genero}-{h_id:07d}"
        return codigo
    else:
        return 'N/A'

def agregar_codigo_heroe(h:dict,h_id:int):
    if(len(h)>0):#valido q no este vacio
        codigo = generar_codigo_heroe(h_id,h['genero'])
        if(len(codigo) == 10):
            h.update({'codigo_heroe':codigo})

def stark_generar_codigo_heroes(h_list:list):
    acum_codes = 0 #acumulador para los codigos
    if(len(h_list)>0):#valido q no sea lista vacia
        tam_h = len(h_list)
        for i in range(tam_h):#itero segun tamaño de lista
            if(type(h_list[i]) == dict and h_list[i]['genero']):#valido q sea dict y tenga un campo genero
                h_list[i].update({'id_heroe':i+1})
                agregar_codigo_heroe(h_list[i],h_list[i]['id_heroe'])
                if(h_list[i]['codigo_heroe']):#si se creo codigo heroe sumo
                    acum_codes+=1
            else:
                print("error!!! origen de datos no desconocido.")
        print(f"se asignaron {acum_codes} codigos.")
        print(f"* primer codigo {h_list[0]['codigo_heroe']}")
        print(f"* ultimo codigo {h_list[-1]['codigo_heroe']}")
    else:
        print("error!!! lista vacia.")

def sanitizar_entero(num_str:str):
    num = num_str.strip()
    match = re.search("[-]?[0-9]+",num)
    if(match):
        if('-' in num):
            return -2
        else:
            try:
                return int(num)
            except(TypeError):
                return -3
    else:
        return -1
    
def sanitizar_flotante(num_str:str):
    num = num_str.strip()
    match = re.search("[-]?[0-9]+[.]?[0-9]+",num)
    if(match):
        if('-' in num):
            return -2
        else:
            try:
                return float(num)
            except(TypeError):
                return -3
    else:
        return -1
    
def sanitizar_str(valor_str:str,default_value='-'):
    #match_num = re.search("\D*",valor_str)
    if(len(valor_str)>0):
        if(valor_str.isalpha()):
            if('/' in valor_str):
                valor_str = valor_str.replace('/','')
            return valor_str.lower()
        
        elif(not valor_str.isalpha()):
            return 'N/A'
    elif('-' not in default_value):
            return default_value.lower()   

def sanitizar_dato(h:dict,h_key:str,tipo_dato:str):
    tipo_dato = tipo_dato.lower()
    h_key = h_key.lower()
    t_datos = ['string','entero','flotante']
    #h_keys = [h.keys()]
    if(len(h)>0):
        if(h_key in h.keys()):
            if(tipo_dato in t_datos):
                if(tipo_dato == 'string'):
                    h[h_key] = sanitizar_str(h[h_key])
                    return True
                elif(tipo_dato == 'entero'):
                    h[h_key] = sanitizar_entero(h[h_key])
                    return True
                elif(tipo_dato == 'flotante'):
                    h[h_key] = sanitizar_flotante(h[h_key])
                    return True
            else:
                print("tipo de dato no reconocido")
        else:
            print("clave inexistente")
    else:
        print("dict vacio")

def stark_normalizar_datos(h_list:list):
    ok = False
    h_keys = ['altura','peso','color_ojos','color_pelo','fuerza','inteligencia']
    if(len(h_list)>0):
        for h in h_list:
            ok1= sanitizar_dato(h,'altura','flotante')
            ok2 = sanitizar_dato(h,'peso','flotante')
            ok3 = sanitizar_dato(h,'color_ojos','string')
            ok4 = sanitizar_dato(h,'color_pelo','string')
            ok5 = sanitizar_dato(h,'fuerza','entero')
            ok6 = sanitizar_dato(h,'inteligencia','string')
        if(ok1 and ok2 and ok3 and ok4 and ok5 and ok6):
            ok = True
        if(ok):
            print("datos normalizados")
    else:
        print("lista vacia")

def generar_indice_nombres(h_list:list):
    flag = False
    index_names = []
    if(len(h_list)>0):
        for h in h_list:
            if(type(h) == dict):
                flag = True
            else:
                print("tipo de dato desconocido")
                flag = False
                break
        if(flag and 'nombre' in h.keys()):
            h_names = list(map(lambda h:h['nombre'],h_list))
            for n in h_names:
                str_seccionado = n.split()
                for str in str_seccionado:
                    index_names.append(str)
        return index_names
    else:
        print("lista vacia")

def stark_imprimir_indice_nombre(h_list:list):
    index_nombres = generar_indice_nombres(h_list)
    large_index = str
    for n in index_nombres:
        large_index = n.join(index_nombres)
        large_index = '-'.join(index_nombres)
    print(large_index)
    
def convertir_cm_a_mts(valor_cm:float):
    #200 cm ~ 2 mts
    if(type(valor_cm) == float):
        if(valor_cm > 0):
            return valor_cm/100
        else:
            return -1
    else:
        print("error tipo de dato")
        return -1
    
def generar_separador(patron:str,largo:int,imprimir=True):
    if((len(patron)>0 and len(patron)<3) and (type(largo) == int and largo>0 and largo<236)):
        separador = patron*largo
        if(imprimir):
            print(separador)
        return separador
    else:
        return 'N/A'
    
def generar_encabezado(titulo:str):
    largo = 150
    generar_separador('*',largo)
    print(titulo.upper())
    generar_separador('*',largo)

def imprimir_ficha_heroe(h:dict):
    generar_encabezado('principal')
    #nombre identidad consultora codigo heroe
    print(f"\tNOMBRE HEROE:\t\t {h['nombre']} ({h['iniciales']})")
    print(f"\tIDENTIDAD SECRETA:\t {h['identidad']}")
    print(f"\tCONSULTORA:\t\t {h['empresa']}")
    print(f"\tCODIGO HEROE:\t\t {h['codigo_heroe']}")
    generar_encabezado('fisico')
    print(f"\tALTURA:\t\t {convertir_cm_a_mts(h['altura']):3.2f} Mtrs.")
    print(f"\tPESO:\t\t {h['peso']:4.2f} Kg.")
    print(f"\tFUERZA:\t\t {h['fuerza']} N")
    generar_encabezado('señas particulares')
    print(f"\tCOLOR OJOS:\t {h['color_ojos']}")
    print(f"\tCOLOR PELO:\t {h['color_pelo']}")

def stark_navegar_fichas(h_list:list):
    index = 0
    loop = True
    imprimir_ficha_heroe(h_list[index])
    while loop:
        print("\n[1]izquierda [S]Salir [2]derecha\n")
        opt = input("ingresar opcion: ")
        opt = opt.upper()
        if((opt.isnumeric() and int(opt)>0 and int(opt)<3) or opt == 'S'):
            match(opt):
                case "1":
                    print("\n")
                    imprimir_ficha_heroe(h_list[index-1])
                    index = index - 1
                    print("\n")
                    pass
                case "2":
                    print("\n")
                    imprimir_ficha_heroe(h_list[index+1])
                    index = index + 1
                    print("\n")
                    pass
                case "S":
                    print('salir')
                    loop = False
                    break 
        else:
            print('error opt incorrecto...')
            print("\n[1]izquierda [S]Salir [2]derecha\n")
            opt = input("ingresar opcion: ")

def imprimir_menu():
    print("""
1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
S - Salir

""")

def stark_menu_principal():
    imprimir_menu()
    print("____________________________________________________________\n")
    opt = input("Ingrese opcion: ")
    print('\n')
    return opt

def stark_marvel_app3(h_list:list):
    flag1 = False
    flag2 = False
    while True:
        os.system('cls')
        opt = stark_menu_principal()
        opt = opt.upper()
        if((opt.isnumeric() and int(opt)>0 and int(opt)<6) or (opt == 'S')):
            match(opt):
                case '1':
                    stark_imprimir_nombres_con_iniciales(h_list)
                case '2':
                    stark_generar_codigo_heroes(h_list)
                    flag1 = True
                case '3':
                    if(flag1):
                        stark_normalizar_datos(h_list)
                        flag2 = True
                case '4':
                    
                    stark_imprimir_indice_nombre(h_list)
                case '5':
                    if(flag2):
                        stark_navegar_fichas(h_list)
                case 'S':
                    print("chau chau")
                    break
        else:
            print("opcion incorrecta. reingrese opcion...")
            opt = input("reingresar...")
        os.system('pause')

