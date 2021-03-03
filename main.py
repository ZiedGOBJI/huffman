import fonctionnalite.arbre.fonction_arbre as fa 
import fonctionnalite.lexique.freqNEW as freq 


#test lexique (étape 1)

nomFichier = input("entrez le nom du fichier à tester :")

a = open("./txt/source/" + nomFichier + ".txt", "r", encoding="utf-8").read()

FreqCroiss = freq.freq(a)

#test construction de l'arbre (étape 2)

liste_nodes = fa.creer_arbre(FreqCroiss)

fa.code("a", liste_nodes)