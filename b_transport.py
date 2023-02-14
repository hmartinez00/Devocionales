from modules.insertar_module import x_transport, last_date, sel_tab


# --------------------------------
# Seteando datos de iniciales
# --------------------------------
database = r"2tim4_1.db"
keys_type = False
ind = 0

ruta_archivo_json = sel_tab(
        keys_type,
        ind,
    )


# key = 'tables'
# tables = setting_routes(key)
# ruta_archivo_json = option_list(tables)

Fecha = last_date(
        keys_type,
        database, 
        ruta_archivo_json
    )

# pregunta = input('Calcular proxima fecha? (S/N): ')

# if pregunta == 's' or pregunta == 'S':
#     table = ruta_archivo_json.split('/')[-1].split('.json')[0]
#     Fecha = selectall(database, table)['Fecha'].iloc[-1]
#     Fecha = DeltaT(Fecha, -1)
# else:
#     Fecha = input('Introduzca la fecha: ')
#     Fecha = format_FechaID(Fecha)

print(Fecha)


# --------------------------------
# Transporte y envio
# --------------------------------

keys_type = False
x_transport(
        keys_type,
        database, 
        ruta_archivo_json, 
        Fecha
    )


# # --------------------------------
# # Leyendo el archivo
# # --------------------------------
# file = r'settings\blackboard\blackboard.txt'

# lines = []
# with open(file, encoding='utf-8') as f:
#     for line in f:
#         lines.append(line.split('\n')[0])
# Tit = lines[0]
# Sub = lines[1]
# Texto_0 = lines[2:]


# # --------------------------------
# # Contruyendo el contenido
# # --------------------------------
# keys_type = input('Desea generar claves automaticas? (S/N): ')

# if keys_type == 's' or keys_type == 'S':
#     tex = [i + 1 for i in range(len(Texto_0))]
#     Texto = Texto_0

# elif keys_type == 'n' or keys_type == 'N':
#     tex = []
#     for i in range(len(Texto_0)):
#         tex.append(Texto_0[i].split(' ')[0])
#     Texto = []
#     for i in Texto_0:
#         new_string = ''
#         for j in i.split(' ')[1:]:
#             new_string = new_string + j + ' '
#         Texto.append(new_string)

# # --------------------------------
# # Contruyendo el diccionario
# # --------------------------------
# sub_param = dict(zip(tex, Texto))

# param = {}
# param["Tit"] = Tit
# param["Sub"] = Sub
# param["Tex"] = sub_param

# # --------------------------------
# # Actualizando json
# # --------------------------------
# with open(ruta_archivo_json) as archivo_json:
#     datos_json = json.load(archivo_json)

# datos_json[Fecha] = param

# with open(ruta_archivo_json, 'w', encoding='utf8') as archivo_json:
#     json.dump(datos_json, archivo_json, indent=4)

# # --------------------------------
# # Importar a la Base de Datos
# # --------------------------------
# importar(database, ruta_archivo_json, Fecha)
# msgo_sender(database, ruta_archivo_json, Fecha)

# # --------------------------------
# # Vaciar registro de Blackboard
# # --------------------------------
# string = ''
# with open(file, 'w', encoding='utf-8') as f:
#     f.write(string)
# f.close()