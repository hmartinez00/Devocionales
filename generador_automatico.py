ruta0 = r'web_assistance\labuenasemilla.py'
ruta1 = r'web_assistance\proverbios.py'
ruta3 = r'b_transport.py'

pregunta = input('Elija mensaje a generar: ')

if      pregunta == '1':
    exec(open(ruta0).read())
elif    pregunta == '2':
    exec(open(ruta1).read())

exec(open(ruta3).read())