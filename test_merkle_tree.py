import unittest
from merkle_tree import *
import time
import pandas as pd
from matplotlib import pyplot as plt
import random
import string
class TestMerkleTree(unittest.TestCase):

    def test_one_tx(self):
        """Test that the tree can construct the proper block header given
        only one transaction
        """
        tx1 = 'a'

        data = tx1 + tx1
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1])

        self.assertEqual(merkle_tree.block_header, data)
        self.assertEqual(merkle_tree.height, 1)

    def test_two_tx(self):
        """Test that the tree can construct the proper block header given
        only two transactions
        """
        tx1 = 'a'
        tx2 = 'b'

        data = tx1 + tx2
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2])

        self.assertEqual(merkle_tree.block_header, data)
        self.assertEqual(merkle_tree.height, 1)


    def test_less_tx(self):
        """Test that the tree can construct the proper block header given
        some non-exponent-of-two amount of transactions
        """
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'

        data1 = tx1 + tx2
        data1 = hash_data(data1, 'sha1')
        data2 = tx3 + tx3
        data2 = hash_data(data2, 'sha1')
        data = data1 + data2
        data = hash_data(data, 'sha1')

        merkle_tree = MerkleTree([tx1, tx2, tx3], 'sha1')

        self.assertEqual(merkle_tree.block_header, data)
        self.assertEqual(merkle_tree.height, 2)

    def test_less_tx_again(self):
        """Test that the tree can construct the proper block header given
        a greater non-exponent-of-two amount of transactions
        """
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'
        tx4 = 'd'
        tx5 = 'e'

        data1 = tx1 + tx2
        data1 = hash_data(data1, 'sha256')
        data2 = tx3 + tx4
        data2 = hash_data(data2, 'sha256')
        data3 = data1 + data2
        data3 = hash_data(data3, 'sha256')
        data4 = tx5 + tx5
        data4 = hash_data(data4, 'sha256')
        data5 = tx5 + tx5
        data5 = hash_data(data5, 'sha256')
        data6 = data4 + data5
        data6 = hash_data(data6, 'sha256')
        data = data3 + data6
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2, tx3, tx4, tx5])

        self.assertEqual(merkle_tree.block_header, data)
        self.assertEqual(merkle_tree.height, 3)

    def test_reset_tree(self):
        """Test that users can wipe the tree successfully"""
        tx1 = 'a'
        tx2 = 'b'

        merkle_tree = MerkleTree([tx1, tx2])
        self.assertEqual(merkle_tree.height, 1)

        merkle_tree.hash_function('sha1')

        merkle_tree.reset_tree()
        self.assertEqual(merkle_tree.height, 0)

    def test_add_tx(self):
        """Test that users can add tx's to the tree successfully. It should
        be reset and reconstructed from the new list
        """
        tx1 = 'a'
        tx2 = 'b'
        tx3 = 'c'
        tx4 = 'd'

        data1 = tx1 + tx2
        data1 = hash_data(data1, 'sha256')
        data2 = tx3 + tx3
        data2 = hash_data(data2, 'sha256')
        data = data1 + data2
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2])
        merkle_tree.add_tx(tx3)

        self.assertEqual(merkle_tree.block_header, data)

        data2 = tx3 + tx4
        data2 = hash_data(data2, 'sha256')
        data = data1 + data2
        data = hash_data(data, 'sha256')

        merkle_tree = MerkleTree([tx1, tx2])
        merkle_tree.add_tx(tx3, tx4)

        self.assertEqual(merkle_tree.block_header, data)

        merkle_tree = MerkleTree([tx1, tx2])
        merkle_tree.add_tx([tx3, tx4])

        self.assertEqual(merkle_tree.block_header, data)

    def test_plotarGraficoMerkleTree(self):
        A = [0]
        for i in range(4):
            inicio = time.time()
            teste = TestMerkleTree()
            teste.test_add_tx()
            fim = time.time()
            print('Tempo de execução:', fim - inicio)
            duracao = fim - inicio
            A.append(duracao )
        plt.plot([1,2,3, 4, 5], A)
        plt.title('--Merkle Tree -- Complexidade Assintótica')
        plt.xlabel("Nodes")
        plt.ylabel("milisegundos executados")
        plt.legend(["Milisegundos", "Nodes"])
        plt.show()

    def test_Plot_500NodesMerkleTree(self):
        A = [0]
        B = []
        tree = MerkleTree(['a','b'])
        for i in range(500):
            inicio = time.time()
            tree.add_tx('z')
            fim = time.time()
            print('Tempo de execução:', fim - inicio)
            duracao = fim - inicio
            if(i<499):
                A.append(duracao)
                B.append(i)

        plt.plot(B[1:499], A[1:499])
        plt.title('--Merkle Tree -- Complexidade Assintótica')
        plt.xlabel("Nodes")
        plt.ylabel("milisegundos executados")
        plt.legend(["Milisegundos", "Nodes"])
        plt.show()


def generate_key_string():
    tokens = string.ascii_uppercase + string.digits #quais caracteres aceitos
    segmentos_char = 5 #numero de caracteres por segmento
    segmentos = 4 #numero de segmentos
    key_string = '' #chave a ser gerada
    for x in range(segmentos):
        key_string += ''.join(random.choice(tokens) 
    for y in range(segmentos_char))
    if x < segmentos-1: 
        key_string += '-' 
        return key_string


if __name__ == '__main__':
     unittest.main()