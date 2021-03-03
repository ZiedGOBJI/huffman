
class Node:

	def __init__(self, label, freq, leftChild=None, rightChild=None):
		self.label = label
		self.freq = freq
		self.leftChild = leftChild
		self.rightChild = rightChild

		if self.rightChild and self.leftChild: #pour gérer le cas de la racine pour la fonction code de fonction_arbre.py
			self.value = 1
		else :
			self.value = 0 



	def get_rightChild(self):
		return self.rightChild

	def get_leftChild(self):
		return self.leftChild

	def get_label(self):
		return self.label

	def get_freq(self):
		return self.freq



