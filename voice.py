import os
from General_Utilities.speech_recognizer import Reconocimiento
from General_Utilities.speech_recognizer import orders

file = 'temp/temp.txt'

if os.path.isfile(file):
    pass
else:
    os.mkdir('temp')
    string = ''
    with open(file, 'w', encoding='utf-8') as f:
        f.write(string)
    f.close()

valor = False

while valor == False:

    try:
        dictado = Reconocimiento()
        
        objeto = orders(file, dictado)
        
        if objeto.close_options():
            break        
        objeto.continue_options()
        objeto.clear()       
    
    except:    
        continue