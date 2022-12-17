from General_Utilities.option_list import option_list
import os

files = os.listdir('settings')

tabla = option_list(files)

print(tabla)