from operator import attrgetter
import fonctionnalite.arbre.classe_arbre as ca 

#création liste de nodes dépareillées

def creer_liste_nodes(FreqCroiss):
	liste_nodes = []
	for t in FreqCroiss:
		liste_nodes.append(ca.Node(t[0],t[1]))

	return liste_nodes


def freq_min(liste_nodes = []):	
	t1 = liste_nodes[0]
	t2 = liste_nodes[1]
	return t1, t2

def nouvel_arbre(sous_arbre_gauche, sous_arbre_droite):
	t1, t2 = sous_arbre_gauche, sous_arbre_droite
	t = ca.Node(t1.get_label() + t2.get_label() , t1.get_freq() + t2.get_freq(), t1, t2)
	return t

#on applique l'algo de huffman, on obtient la racine de l'arbre
def creer_arbre(FreqCroiss):
	liste_nodes = creer_liste_nodes(FreqCroiss) 

	while len(liste_nodes)>1:
		liste_nodes = sorted(liste_nodes, key=attrgetter("freq","label"))
		t1, t2 = freq_min(liste_nodes)
		liste_nodes.append(nouvel_arbre(t1, t2))
		liste_nodes.pop(liste_nodes.index(t1))
		liste_nodes.pop(liste_nodes.index(t2))

	return liste_nodes	

################################################################################################################

def code(caractere, liste_nodes):

	
	code_binaire = []
#pour le pere direct 

	for node1 in liste_nodes:

		if node1.leftChild.get_label() == caractere:
			code_binaire.append(0)
			pere = node1   #pas de soucis car le pere est unique (arbre binaire)

		if node1.rightChild.get_label() == caractere:
			code_binaire.append(1)  
			pere = node1 

#tous les grands-parents

	for node2 in liste_nodes:

		if node2.leftChild.get_label() == pere.get_label():
			code_binaire.append(0)
			pere = node2   

		if node2.rightChild.get_label() == pere.get_label():
			code_binaire.append(1)  
			pere = node2

	code = str(code_binaire)
	print(code)





























'''
[(n1),(n2),(n3),(n4)] 

parametres : caractere

caractere -> node 

code_binaire = [] 
liste_nodes_voisines = [node]

for k in range(len(liste_nodes_voisines))

if node.get_rightChild() not None:
		code_binaire.append(1)
		liste_nodes_voisines.append()

if node.get_leftChild() not None:
		code_binaire.append(0)

code = join(code_binaire)

return code  
'''



