class strmsgformat:

    def __init__(
        self,
        __table__,
        __date__,
        __title__,
        __Sub__,
        __text__,
    ):
        self.__table__ = __table__
        self.__date__ = __date__
        self.__title__ = __title__
        self.__Sub__ = __Sub__
        self.__text__ = __text__

    def msgtext(self):

        if self.__table__ == 'aguas_vivas_pasajes':

            send_pasaje = f"*{self.__title__}*\n" + f"*{self.__Sub__}*\n" + f"\n{self.__text__}"

        elif self.__table__ == 'aguas_vivas_comentarios':

            send_pasaje = f"*{self.__title__}*\n" + f"*{self.__Sub__}" + " _(Comentario:)_*\n" + f"\n{self.__text__}"

        return send_pasaje