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
    
    f = open(file, 'r')
    string = f.read()
    f.close()
    
    string = string + str(dictado) + '\n'

    f = open(file, 'w')
    f.write(string)
    f.close()
    
    valor = True