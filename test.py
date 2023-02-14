from General_Utilities.menu import menu

# key = 'sub_exec'
# sub_key = 'web_assistance'
key = None
sub_key = None
menu()


# import json
# from General_Utilities.control_rutas import setting_routes


# key = "sub_exec"
# sub_key = 'web_assistance'

# file_routes = 'settings/routes/routes.json'

# with open(file_routes) as archivo_json:
#     datos_json = json.load(archivo_json)

# ruta_archivo = []
# for i in datos_json[key]:
#     ruta_archivo.append(i)

# print(datos_json[key]['web_assistance']['acciones'])

# def menu(key = None):

#     if key == None:
#         key = 'exec'
#         opciones = setting_routes(key)[0]
#         acciones = setting_routes(key)[1]
    
#     elif key != None:
#         opciones = setting_routes(key)["web_assistance"][0]
#         acciones = setting_routes(key)["web_assistance"][1]

#     lista = [opciones, acciones] 

#     return lista

# key = 'sub_exec'
# opciones = setting_routes(key)
# print(opciones)