#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na classe Livraria sub-classes Revista e Livro sabemos que:
# atributos: nome, Número de páginas, Idioma, Editora, tipo e status
# todos atributos encapsulados fortemente
# métodos para:
# controlar o aluguel dos livros, calculo do aluguel em (07)dias
# controlar a venda dos livros
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Sempre que acontecer um aluguel ou venda diminuir do estoque.
# OBS: Faça a impressão dos elementos

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
    def __init__(self, nome, tipo, numero_de_paginas,idioma,editora,status):
        super().__init__(nome, tipo)
        self.__numero_de_paginas = numero_de_paginas
        self.__idioma = idioma
        self.__editora = editora
        self.__status = status

    #------------------GETS AND SETERS
    @property
    def numero_de_paginas(self):
        return self.__numero_de_paginas
    
    @property
    def idioma(self):
        return self.__idioma

    @property
    def editora(self):
        return self.__editora
    
    @property
    def status(self):
        return self.__status
    
    @numero_de_paginas.setter
    def numero_de_paginas(self, novo_numero):
        if abs(type(novo_numero)) == int: 
            self.__numero_de_paginas = novo_numero
        else:
            print('Digite um valor valido, int()')
    
    @idioma.setter
    def idioma(self, novo_idioma):
        if type(novo_idioma) == str: 
            self.__idioma = novo_idioma
        else:
            print('Digite um valor valido, str()')
    
    @editora.setter
    def editora(self, novo_nome):
        if type(novo_nome) == str: 
            self.__editora = novo_nome
        else:
            print('Digite um valor valido, str()')

    @status.setter
    def status(self, novo_nome):
        if type(novo_nome) == str: 
            self.__status = novo_nome
        else:
            print('Digite um valor valido, str()')
        
class Livro(Livraria):
    def __init__(self, nome, tipo,numero_de_paginas,idioma,editora,status):
        super().__init__(nome, tipo)
        self.__numero_de_paginas = numero_de_paginas
        self.__idioma = idioma
        self.__editora = editora
        self.__status = status
    
    #------------------GETS AND SETERS
    @property
    def numero_de_paginas(self):
        return self.__numero_de_paginas
    
    @property
    def idioma(self):
        return self.__idioma

    @property
    def editora(self):
        return self.__editora
    
    @property
    def status(self):
        return self.__status
    
    @numero_de_paginas.setter
    def numero_de_paginas(self, novo_numero):
        if abs(type(novo_numero)) == int: 
            self.__numero_de_paginas = novo_numero
        else:
            print('Digite um valor valido, int()')
    
    @idioma.setter
    def idioma(self, novo_idioma):
        if type(novo_idioma) == str: 
            self.__idioma = novo_idioma
        else:
            print('Digite um valor valido, str()')
    
    @editora.setter
    def editora(self, novo_nome):
        if type(novo_nome) == str: 
            self.__editora = novo_nome
        else:
            print('Digite um valor valido, str()')

    @status.setter
    def status(self, novo_nome):
        if type(novo_nome) == str: 
            self.__status = novo_nome
        else:
            print('Digite um valor valido, str()')