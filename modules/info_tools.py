def str_estract(__cadena__, __sub_start__, __sub_end__):
    '''
    Arroja una lista de los valores de las etiquetas con atributos coincidentes con la subcadena.
    '''
    __vers__ = []
    __ref__ = []
    while True:
        ocr = str(__cadena__).find(__sub_start__)
        if ocr != -1:
            __cadena__ = str(__cadena__)[ocr + len(__sub_start__):]
            __s_ref__ = __cadena__.split(__sub_end__)[0]
            if __s_ref__ not in __ref__:
                __ref__.append(__s_ref__)
            __num__ = __cadena__.split('-')[2].split(__sub_end__)[0]
            __res__ = str(__cadena__).split('>')[3].split('<')[0]
            __string__ = f'{__num__} {__res__}'
            __vers__.append(__string__)
        elif ocr == -1:
            break
    
    return __vers__, __ref__

def str_title(__cadena__):
    '''
    Arroja una lista de los valores de las etiquetas con atributos coincidentes con la subcadena.
    '''
    # Extraemos el titulo
    __string__ = str(__cadena__).split('>')[2].split('<')[0]
    __vers__ = __string__

    # Extraemos la referecia
    __string__ = str(__cadena__).split('class="text ')[1].split('"')[0]
    __ref__ = __string__

    res = [__ref__, __vers__]
    
    return res

def general_estract(__cadena__, __sub_start__, __sub_end__):
    '''
    Arroja una lista de los valores de las etiquetas con atributos coincidentes con la subcadena.
    '''
    ocr = str(__cadena__).find(__sub_start__)
    __cadena__ = str(__cadena__)[ocr + len(__sub_start__):]
    __string__ = str(__cadena__)#.split(__sub_end__)[0]
    
    return __string__