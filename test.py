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
    dictado = Reconocimiento()
    
    if 'finalizar dictado' in dictado:
        valor = True
    
    f = open(file, 'r')
    string = f.read()
    f.close()
    
    if 'nueva línea' in dictado:
        string = string + str(dictado) + '\n'
    else:
        string = string + str(dictado)

    f = open(file, 'w')
    f.write(string)
    f.close()
    