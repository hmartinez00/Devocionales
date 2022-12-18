import os
import subprocess
from General_Utilities.option_list import option_list

subprocess.run('clear')

opciones = [
	'Crear tabla',
	'Actualizar json de importacion',
	'Insertar renglon',
	'Generar mensajes',
	'Salir',
]

opcion = option_list(opciones)

if opcion==opciones[0]:
	exec(open("crear_tabla.py").read())
elif opcion==opciones[1]:
	exec(open("transporte.py").read())
elif opcion==opciones[2]:
	exec(open("insertar.py").read())
elif opcion==opciones[3]:
	exec(open("msgo_creator.py").read())
elif opcion==opciones[4]:
	print('Adios!')
else:
	print('\nOpcion Invalida! Repita la eleccion.\n')
	exec(open("menu.py").read())