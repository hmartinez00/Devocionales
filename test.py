from General_Utilities.speech_recognizer import Reconocimiento

valor = False

while valor == False:
    Reconocimiento()
    pregunta = input('\nCoincide con lo dicho? (S/N): ')
    if pregunta == 's' or pregunta == 'S':
        valor = True
    elif pregunta == 'n' or pregunta == 'N':
        continue