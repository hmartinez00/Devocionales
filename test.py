from General_Utilities.speech_recognizer import Reconocimiento

file = 'tmp.txt'

string = ''

f = open(file, 'w')
f.write(string)
f.close()

valor = False

while valor == False:
    dictado = Reconocimiento()
    pregunta = input('\nCoincide con lo dicho? (S/N): ')
    if pregunta == 's' or pregunta == 'S':

        f = open(file, 'r')
        string = f.read()
        f.close()

        string = string + str(dictado)

        f = open(file, 'w')
        f.write(string)
        f.close()

        valor = True
    elif pregunta == 'n' or pregunta == 'N':
        continue