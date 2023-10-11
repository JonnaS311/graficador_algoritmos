class Ciudad:

    def __init__(self, nombre, id, distancia_destino):
        self.__nombre = nombre
        self.__id = id
        self.__distancia_destino = distancia_destino

    @property
    def nombre(self):
        return self.__nombre

    @property
    def id(self):
        return self.__id

    @property
    def destino(self):
        return self.__distancia_destino

    def __repr__(self):
        return f'{self.__nombre}'