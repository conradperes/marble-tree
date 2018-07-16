
class Node:
	"""Classe de implementação de nó empacotado ou wrapper. 
	Útil para rastrear a profundidade dos nós na construção 
	da prova de Merkle"""
	def __init__(self, direction, tx):
		self._direction = direction
		self._tx = tx

	def __eq__(self, other):
		"""Substitui a implementação default"""
		if isinstance(self, other.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __cmp__(self, other):
		"""Substitui a implementação default"""
		if isinstance(self, other.__class__):
			return self.__dict__ == other.__dict__
		return False
	

	@property
	def direction(self):
		"""int: Permite pesquisar nós em profundidade"""
		return self._direction

	@property
	def tx(self):
		"""string: Permite pesquisar nós pelo texto da string"""
		return self._tx
