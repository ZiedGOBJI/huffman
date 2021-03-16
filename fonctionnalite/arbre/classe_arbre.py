
class Node:

	def __init__(self, label, freq, leftChild=None, rightChild=None):
		self.label = label
		self.freq = freq
		self.leftChild = leftChild
		self.rightChild = rightChild

	def getrightChild(self):
		#obtenir l'enfant de droite
		return self.rightChild

	def getleftChild(self):
		#obtenir l'enfant de gauche
		return self.leftChild

	def getLabel(self):
		#obtenir le label
		return self.label

	def getFreq(self):
		#obtenir l'occurence
		return self.freq

	def isFeuille(self):
		#savoir si c'est une feuille ou pas
		if self.leftChild is None and self.rightChild is None:
			return(True)
		else:
			return(False)
 
	def getChilds():
		#obtenir les enfants
		return self.getleftChild(), self.getrightChild()
		
	def getPath(self, node):
		#obtenir le chemin parcouru pour arriver à une feuille
		path = []
		listeChild = self.getChilds()

		while self!= node:
			for nodes in listeChild:
				if(nodes.getleftChild() == node or nodes.getrightChild() == node):
					path.append(node)
					node = nodes 
		path.append(self)
		path.reverse()

		return(path)	# [root, root child, root grand-child, node]
