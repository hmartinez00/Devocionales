import json
from ManageDB.sqlite_on_db import *
from modules.msgo_creator_module import msgo_sender


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