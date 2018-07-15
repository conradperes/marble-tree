# Prova Merkle e Verificação

## Introdução

Árvore Merkle é uma estrutura de dados baseada em hash usada para provar a integridade de uma transação de dados armazenadados em blovo. **Para esse algoritmo assuma que as árvores são binárias, balanceadas, e que o número de transações serão armazenadas são algum exponde de dois.**

![Merkle Tree](img/merkle_tree.jpeg "Merkle Tree")
_Source: [Grid+](https://blog.gridplus.io/efficiently-bridging-evm-blockchains-8421504e9ced)_

Acima você poderá ver como a árvore se parece. As oito transações no bloco (A-H) estão alinhadas no campo transactions. O segundo campo contém 4 hashes (S(X) = sha3 hash) de transações filhas. O terceiro campo contém hashes de hashes filhos, e a raiz contém um hash de hashes de hashes das transações. Genericamente, isso é como parte da transação de bloco de Ethereum concentrado na raiz aonde nós conhecemos como transação header (uma das 15 peças de informação que vai no bloco header).

## O Problema

The reason we use Merkle trees to store block data (i.e. transactions) is that verification is very efficient. This verification is called a Merkle proof.

Suppose we want to prove that transaction C was indeed in the block that formed the header shown above.

![Merkle Proof](img/merkle_proof.jpeg "Merkle Proof")
_Source: [Grid+](https://blog.gridplus.io/efficiently-bridging-evm-blockchains-8421504e9ced)_

In addition to the transaction hash C , we also need D, S(A,B), and S(S(E,F),S(G,H)) to form the proof. The verification itself performs the following steps on the proof:

* Hash C and D to produce S(C,D).
* Hash S(A,B) and S(C,D) to produce S(S(A,B),S(C,D)).
* Hash S(S(A,B),S(C,D)) and S(S(E,F),S(G,H)) to produce the root.
* Check that the root is the same as what has been stored previously.

The efficiency here is that we proved a transaction belonged in a block with only 3 accompanying pieces of information (instead of the 7 other transactions that were stored in the block). This efficiency becomes exponentially more pronounced with larger trees.

It will be your job to implement the Merkle proof functionality and to verify it.

### A Note on Project Layout

You need only to make changes to `merkle_proof.py`, please make sure to familiarize yourselves with the layout of the entire directory however. The roles of the other files are as follows:

* `hash_data_structures.py`: contains intermediary object classes that act as nodes in the tree.
* `merkle_tree.py`: contains the Merkle Tree implementation; make sure you familiarize yourself with how it works. It takes in a list of transactions as inputs. Transactions are generally in the form of strings in this case, for brevity.
* `test.py`: a script to help run all the other tests.
* `test_*.py`: testing scripts built on the `unittest` module. Each test ensures the integrity of their respective file.
* `test_sanity.py`: tests that highlight the basic use of each data structure. Take a look at this file if you find yourself lost on how they are implemented.
* `utils.py`: contains multiple helpful methods.

## Running Tests

Use `python3 test.py` to run all the tests. You may add your own tests and run them with `python [filename].py`. Make sure to format tests according to the `unittest` module (take a look at the other files to see examples).

Writing your own tests is not required but highly recommended. All that matters is you pass our internal test cases.

