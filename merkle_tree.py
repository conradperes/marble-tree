from hash_data_structures import *


class MerkleTree(object):
    """Implementação Merkle Tree , função hash default é 'sha256'.
    Nós são contruídos a cada adição de txt com a lista de txt persistentes
    """
    def __init__(self, tx_list, hash_function='sha256'):
        hash_function = hash_function.lower()
        assert tx_list, "No transactions to be hashed"
        assert hash_function in SECURE_HASH_FUNCTIONS, (
            "{} is not a valid hash function".format(hash_function))
        self._hash_function = hash_function
        self._leaves = tx_list
        self._nodes = []
        self._root = self._evaluate()
        self._height = self._root.height
        self._block_header = self._root.data

    def add_tx(self, *tx):
        """Adiciona um quantidade de textos na árvore. 
        Precisa ser reconstruído toda vez que acontece uma mudança no block header
        """
        tx_in = list(tx)
        if type(tx_in[0]) == list:
            tx_in = tx_in[0]
        self._leaves += tx_in
        self._reevaluate()

    def reset_tree(self, hash_function='sha256'):
        """Limpa dados da árvore"""
        self._hash_function = hash_function
        self._nodes = []
        self._height = 0
        self._block_header = None

    def _evaluate(self):
        """Usado para construir a árvore e chegar ao bloco header"""
        leaves = list(self._leaves)
        if not is_power_of_two(len(leaves)) or len(leaves) < 2:
            last_tx = leaves[-1]
            while not is_power_of_two(len(leaves)) or len(leaves) < 2:
                leaves.append(last_tx)
        for tx in range(0, len(leaves), 2):
            self._nodes.append(HashLeaf(leaves[tx], leaves[tx+1],
                self._hash_function))
        nodes = list(self._nodes)
        while len(nodes) > 2:
            left = nodes.pop(0)
            right = nodes.pop(0)
            node = HashNode(left, right, self._hash_function)
            nodes.append(node)
        if len(nodes) == 1:
            return nodes[0]
        return HashNode(nodes[0], nodes[1], self._hash_function)

    def _reevaluate(self):
        """Reseta a árvore fazendo a chamada a `_evaluate(...)` to reconstruct
        a árvore dada a lista de tx's persistente
        """
        self.reset_tree(self._hash_function)
        self._root = self._evaluate()
        self._height = self._root.height
        self._block_header = self._root.data

    @property
    def hash_function(self):
        """func: Permite ao usuário consultar a função hash da árvore"""
        return self._hash_function

    # @hash_function.setter
    def hash_function(self, value):
        """Permite ao usuário mudar a funcão hash da árvore. 
        Requer que a árvore seja reconstruída para acomodar essa mudança
        """
        value = value.lower()
        assert value in SECURE_HASH_FUNCTIONS, (
            "{} não é uma função hash válida".format(value))
        self._hash_function = value

    @property
    def block_header(self):
        """str: Permite ao usuário pesquisar o header da árvore bloqueado com hash"""
        return self._block_header

    @property
    def height(self):
        """int: Permite ao usuário pesquisar a altura da árvore"""
        return self._height

    @property
    def leaves(self):
        """list: Permite ao usuário pesquisar a lista de  tx's  da árvore"""
        return self._leaves
