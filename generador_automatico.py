from modules.insertar_module import x_transport, last_date, sel_tab


ruta0 = r'web_assistance\labuenasemilla.py'
ruta1 = r'web_assistance\proverbios.py'

# database = r"2tim4_1.db"
# keys_type = True
# ind = 4

# ruta_archivo_json = sel_tab(
#         keys_type,
#         ind,
#     )

# Fecha = last_date(
#         keys_type,
#         database, 
#         ruta_archivo_json
#     ).replace('-', '')

# print(
#         ruta_archivo_json,
#         Fecha
#     )

# ruta0 = r'web_assistance\labuenasemilla.py'
# ruta1 = r'web_assistance\proverbios.py'
# ruta3 = r'b_transport.py'

pregunta = input('Elija mensaje a generar: ')

if      pregunta == '1':
    exec(open(ruta0).read())
elif    pregunta == '2':
    exec(open(ruta1).read())

# x_transport(
#         keys_type,
#         database, 
#         ruta_archivo_json, 
#         Fecha
#     )