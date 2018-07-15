from utils import *


SECURE_HASH_FUNCTIONS = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']

class HashLeaf(object):
    """Anexar dois pedaços de string e armazenar o hash de strings concatenadas
    """
    def __init__(self, left, right, hash_function):
        assert isinstance(hash_function, str), (
            "Função Hash não é do tipo `String`")
        self._hash_function = hash_function
        self._left = left
        self._right = right
        self._data = self._evaluate()
        self._height = 1
        
    def _evaluate(self):
        """Assegure mandar o dado do tipo string"""
        assert isinstance(self._left, str), "Data is not of type `String`"
        assert isinstance(self._right, str), "Data is not of type `String`"
        return hash_data(self._left + self._right, self._hash_function)

    @property
    def data(self):
        """str: Permite ao usuário pesquisar o dado armazenado em hash
        no nó folha=HashLeaf
        """
        return self._data

    @property
    def height(self):
        """int: Permite ao usuário pesquisar a altura do dado armazenado em hash
        no nó folha=HashLeaf"""
        return self._height

class HashNode(HashLeaf):
    """Anexa duas estruturas de HashLeaf e armazena o hash do seu concatenamento
    data
    """
    def __init__(self, left, right, hash_function):
        super().__init__(left, right, hash_function)
        assert left._hash_function == hash_function, (
            "Funções Hash incompatíveis")
        assert right._hash_function == hash_function, (
            "Funções Hash incompatíveis")
        self._height = self._left.height + 1

    def _evaluate(self):
        """Assegure que o dado esta na forma da estrutura de dados HashLeaf e tem
        a altura correta. Separa método de `HashLeaf` como esta em diferentes 
        requerimentos
        """
        assert isinstance(self._left, HashLeaf), (
            "Dado não é do tipo `HashLeaf`")
        assert isinstance(self._right, HashLeaf), (
            "Dado não é do tipo `HashLeaf`")
        assert self._left.height == self._right.height, (
            "Ramo/nó da esquerda ou direita não esta balanceado")
        return hash_data(self._left.data + self._right.data,
            self._hash_function)
