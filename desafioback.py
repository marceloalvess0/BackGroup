class Livraria():
    pass
    def __init__(self,nome,tipo):
        self.__nome=nome
        self.__tipo=tipo
        pass
    @property 
    def nome(self) :
        return self.__nome
    @nome.setter 
    def nome (self,novo_nome):
        if type(novo_nome) == str() :
            self.__nome = novo_nome
        else:
            print('Novo nome invalido, digite algo valido')
    @property
    def tipo (self) :
        return self.__tipo
    @tipo.setter
    def tipo (self,novo_tipo) :
        if type(novo_tipo) == str() :
            self.__tipo = novo_tipo
        else:
            print('Novo tipo invalido, digite algo valido')
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