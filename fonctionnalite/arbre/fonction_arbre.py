from operator import attrgetter
import fonctionnalite.arbre.classe_arbre as ca 


def creerlisteNodes(freqCroiss):
	#créer les noeuds des caractères, donc les feuilles
	listeNodes = []
	for t in freqCroiss:
		listeNodes.append(ca.Node(t[0],t[1]))

	return listeNodes

def freqMin(listeNodes = []):	
	#on trouve les noeuds des 2 caractères ayant le moins d'occurence
	t1 = listeNodes[0]
	t2 = listeNodes[1]
	return t1, t2


def nouvelArbre(sousarbreGauche, sousarbreDroite):
#on crée un nouveau noeud, qui sera une racine locale d'un sous-arbre, ce noeud est construit selon la somme des 2 fréquences minimales déterminées grâce à freq_min()
	t1, t2 = sousarbreGauche, sousarbreDroite
	t = ca.Node(t1.getLabel() + t2.getLabel(), t1.getFreq() + t2.getFreq(), t1, t2)
	return t


def creerArbre(freqCroiss):
	#on applique l'algo de huffman, on obtient la racine de l'arbre
	listeNodes = creerlisteNodes(freqCroiss) 


	while len(listeNodes)>1:
		listeNodes = sorted(listeNodes, key=attrgetter("freq","label"))
		t1, t2 = freqMin(listeNodes)

		listeNodes.append(nouvelArbre(t2, t1))

		listeNodes.pop(listeNodes.index(t1))
		listeNodes.pop(listeNodes.index(t2))

	root = listeNodes[0] 

	return root 




