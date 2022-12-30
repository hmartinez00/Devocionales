import os
from General_Utilities.speech_recognizer import Reconocimiento

file = 'tmp.txt'

if os.path.isfile(file):
    pass
else:
    string = ''
    f = open(file, 'w')
    f.write(string)
    f.close()

valor = False

while valor == False:

    try:
        dictado = Reconocimiento()
        
        if 'finalizar dictado' in dictado:
            break
        
        f = open(file, 'r')
        string = f.read()
        f.close()
        
        if 'nueva línea' in dictado:
            string = string + '\n'
        elif 'nuevo párrafo' in dictado:
            string = string + '\n\n'
        elif 'borrar todo' in dictado:
            string = ''
            f = open(file, 'w')
            f.write(string)
            f.close()
        else:
            string = string + ' ' + str(dictado)

        f = open(file, 'w')
        f.write(string)
        f.close()
    
    except:    
        continue