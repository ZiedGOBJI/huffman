
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

	def is_feuille(self):
		if self.leftChild is None and self.rightChild is None:
			return(True)
		else:
			return(False)

	def get_childs():
		return self.get_leftChild(), self.get_rightChild()
		

	def get_path(self, node):

		path = []
		liste_child = self.get_liste_child()

		while self!= node:
			for nodes in liste_child:
				if(nodes.get_leftChild() == node or nodes.get_rightChild() == node):
					path.append(node)
					node = nodes 
		path.append(self)
		path.reverse()

		return(path)	# [root, root child, root grand-child, node]
