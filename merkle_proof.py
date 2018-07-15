from utils import *
import math
from node import Node
from merkle_tree import *

SECURE_HASH_FUNCTIONS = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']

def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    #### YOUR CODE HERE
    return merkle_tree._leaves
    




def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """
    #### YOUR CODE HERE
    #letra = ''
    merkle_tree = MerkleTree(merkle_proof)
    #for letras in merkle_proof:
    #    letra = letra + letras
    print('merkle_tree.block_header:',merkle_tree.block_header)
    return merkle_tree.block_header


    
