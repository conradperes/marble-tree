from utils import *
import math
from node import Node
from merkle_tree import *

SECURE_HASH_FUNCTIONS = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']

def merkle_proof(tx, merkle_tree):
    """

    Return lista de dados dos nós da árvore sem hash
    """
    #### YOUR CODE HERE
    return merkle_tree._leaves
    




def verify_proof(tx, merkle_proof):
   
    merkle_tree = MerkleTree(merkle_proof)
    print('merkle_tree.block_header:',merkle_tree.block_header)
    return merkle_tree.block_header


    
