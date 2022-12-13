class Livraria():
    pass
    def __init__(self,nome,tipo):
        self.__nome=nome
        self.__tipo=tipo
        pass
class Revista(Livraria):
    def __init__(self, nome,numero_de_paginas,idioma,editora,status):
        super().__init__(nome)
        self.__numero_de_paginas=numero_de_paginas
        self.__idioma = idioma
        self.__editora = editora
        self.__status = status
    pass
class Livro(Livraria):
    def __init__(self, nome, tipo,numero_de_paginas,idioma,editora,status):
        super().__init__(nome, tipo)
        self.__numero_de_paginas=numero_de_paginas
        self.__idioma = idioma
        self.__editora = editora
        self.__status = status
    pass