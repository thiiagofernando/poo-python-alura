from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
            
            
    @property 
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self,cliente, nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)