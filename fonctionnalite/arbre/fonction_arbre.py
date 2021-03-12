from operator import attrgetter
import fonctionnalite.arbre.classe_arbre as ca 


#créer les noeuds des caractères, donc les feuilles
def creer_liste_nodes(FreqCroiss):
	liste_nodes = []
	for t in FreqCroiss:
		liste_nodes.append(ca.Node(t[0],t[1]))

	return liste_nodes

#on trouve les noeuds des 2 caractères ayant le moins d'occurence
def freq_min(liste_nodes = []):	
	t1 = liste_nodes[0]
	t2 = liste_nodes[1]
	return t1, t2

#on crée un nouveau noeud, qui sera une racine locale d'un sous-arbre, ce noeud est construit selon la somme 
#des 2 fréquences minimales déterminées grâce à freq_min()
def nouvel_arbre(sous_arbre_gauche, sous_arbre_droite):
	t1, t2 = sous_arbre_gauche, sous_arbre_droite
	t = ca.Node(t1.get_label() + t2.get_label(), t1.get_freq() + t2.get_freq(), t1, t2)
	return t

#on applique l'algo de huffman, on obtient la racine de l'arbre
def creer_arbre(FreqCroiss):
	liste_nodes = creer_liste_nodes(FreqCroiss) 


	while len(liste_nodes)>1:
		liste_nodes = sorted(liste_nodes, key=attrgetter("freq","label"))
		t1, t2 = freq_min(liste_nodes)

		liste_nodes.append(nouvel_arbre(t2, t1))

		liste_nodes.pop(liste_nodes.index(t1))
		liste_nodes.pop(liste_nodes.index(t2))

	root = liste_nodes[0] 

	return root 




