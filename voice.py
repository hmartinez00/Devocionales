import os
from tkinter import filedialog
from Eliezer.voice import recognizer


ruta = os.getcwd()
name = 'voice_comand_settings.json'
for ruta, _, archivos in os.walk('.'):
    for archivo in archivos:
        if archivo == name:
            ruta_archivo_json = os.path.join(ruta, archivo)

file = filedialog.askopenfilename()

recognizer(ruta_archivo_json, file)