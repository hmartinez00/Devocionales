import json
from ManageDB.sqlite_on_db import *
from modules.msgo_creator_module import msgo_sender
from General_Utilities.fecha import format_FechaID, DeltaT
from General_Utilities.control_rutas import setting_routes
from General_Utilities.option_list import option_list


def importar(database, ruta_archivo_json, Fecha):

    table = ruta_archivo_json.split('/')[-1].split('.')[0]

    print(ruta_archivo_json)


    with open(ruta_archivo_json) as archivo_json:
        datos_json = json.load(archivo_json)

    Tit = datos_json[Fecha]["Tit"]
    Sub = datos_json[Fecha]["Sub"]
    Tex = datos_json[Fecha]["Tex"]

    for i in Tex.keys():
        texto = f'{i}. {Tex[i]}'

        renglon = (
            Fecha,
            Tit,
            Sub,
            texto
        )

        insert(database, table, renglon)

def x_transport(
        keys_type: bool,
        database: str, 
        ruta_archivo_json: str, 
        Fecha: str
    ):

    '''
    Funcion de transporte del contenido del Blackboard para actualizar el contenido de los json y transportar automaticamente a la Base de datos
    
    *parameters:
        keys_type: bool. Cuando esta en True, genera la claves automaticamente. Si es False, toma las claves del texto.
        database: str. Nombre de la base de datos a la que se desea conectar.
        ruta_archivo_json: str. Nombre del json que sirve para transportar los datos a la tabla.
        Fecha: str. La fecha que se usa como clave para indexar la informacion en el json.
    

    '''

    # --------------------------------
    # Leyendo el archivo
    # --------------------------------
    file = r'settings\blackboard\blackboard.txt'

    lines = []
    with open(file, encoding='utf-8') as f:
        for line in f:
            lines.append(line.split('\n')[0])
    Tit = lines[0]
    Sub = lines[1]
    Texto_0 = lines[2:]

    # --------------------------------
    # Contruyendo el contenido
    # --------------------------------
    if keys_type == True:
        tex = [i + 1 for i in range(len(Texto_0))]
        Texto = Texto_0

    elif keys_type == False:
        # --------------------------------
        # Contruyendo el contenido
        # --------------------------------
        keys_type = input('Desea generar claves automaticas? (S/N): ')

        if keys_type == 's' or keys_type == 'S':
            tex = [i + 1 for i in range(len(Texto_0))]
            Texto = Texto_0

        elif keys_type == 'n' or keys_type == 'N':
            tex = []
            for i in range(len(Texto_0)):
                tex.append(Texto_0[i].split(' ')[0])
            Texto = []
            for i in Texto_0:
                new_string = ''
                for j in i.split(' ')[1:]:
                    new_string = new_string + j + ' '
                Texto.append(new_string)

        # --------------------------------
    
    # --------------------------------
    # Contruyendo el diccionario
    # --------------------------------
    sub_param = dict(zip(tex, Texto))

    param = {}
    param["Tit"] = Tit
    param["Sub"] = Sub
    param["Tex"] = sub_param

    # --------------------------------
    # Actualizando json
    # --------------------------------
    with open(ruta_archivo_json) as archivo_json:
        datos_json = json.load(archivo_json)

    datos_json[Fecha] = param

    with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
        json.dump(datos_json, archivo_json, indent=4)

    # --------------------------------
    # Importar a la Base de Datos
    # --------------------------------
    importar(database, ruta_archivo_json, Fecha)
    msgo_sender(database, ruta_archivo_json, Fecha)

    # --------------------------------
    # Vaciar registro de Blackboard
    # --------------------------------
    string = ''
    with open(file, 'w', encoding='utf-8') as f:
        f.write(string)
    f.close()

def last_date(
        keys_type: bool,
        database: str, 
        ruta_archivo_json: str, 
    ):

    '''
    Funcion para extraccion de ultima fecha.

    *parameters:
        keys_type: bool. Cuando esta en True, selecciona automaticamente la ultima fecha de la tabla. Si es False, pregunta.
        database: str. Nombre de la base de datos a la que se desea conectar.
        ruta_archivo_json: str. Nombre del json que sirve para transportar los datos a la tabla.
        table: str. Nobre de la tabla a consultar.

    '''

    if keys_type == True:
        table = ruta_archivo_json.split('/')[-1].split('.json')[0]
        Fecha = selectall(database, table)['Fecha'].iloc[-1]
        Fecha = DeltaT(Fecha, -1)

    elif keys_type == False:
        pregunta = input('Calcular proxima fecha? (S/N): ')

        if pregunta == 's' or pregunta == 'S':
            table = ruta_archivo_json.split('/')[-1].split('.json')[0]
            Fecha = selectall(database, table)['Fecha'].iloc[-1]
            Fecha = DeltaT(Fecha, -1)
        else:
            Fecha = input('Introduzca la fecha: ')
            Fecha = format_FechaID(Fecha)
    
    return Fecha

def sel_tab(
        keys_type: bool, 
        ind: int
    ):

    '''
    Funcion para seleccion automatica de tablas

    *parameters:
        keys_type: str. Cuando esta en True, selecciona automaticamente la tabla segun el parametro "ind". Si es False, pregunta.
        ind: int. Numero de la tabla en la lista tablas.
    
    '''

    key = 'tables'
    
    if keys_type == True:
        tables = setting_routes(key)[ind]
        ruta_archivo_json = tables
    
    elif keys_type == False:
        tables = setting_routes(key)
        ruta_archivo_json = option_list(tables)

    return ruta_archivo_json