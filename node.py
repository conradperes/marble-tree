
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
		"""int: Allow user to query node for its depth"""
		return self._direction

	@property
	def tx(self):
		"""string: Allow user to query node for its tx string"""
		return self._tx
