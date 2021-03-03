from operator import itemgetter

#return un fichier .txt avec le résultat
def freq(texte):
	freq = []
	lettres = []
	occurences = []

	for lettre in texte:
		if lettre not in lettres:
			lettres.append(lettre)

	alphabet = lettres.sort()

	for k in lettres:
#utilisation de la méthode count() pour compter le nombre de fois où la lettre apparaît dans le texte
		occurences.append(texte.count(k))

	for i in range(len(lettres)):
#on choisit la liste "lettres" pour le premier élément du tuple pour faciliter la détermination du 2eme élément du tuple "occurences" 
		freq.append((lettres[i],occurences[i]))

#on trie d'abord par l'élément "1" (fréquences) puis par l'élément "0" (ordre caractères ascii)
	FreqCroiss = sorted(freq, key=itemgetter(1,0))

#Mise en forme conforme
	f = open("./txt/lexique/lexique.txt", "w")
	f.write(str(len(lettres)) + "\n")

	for tuples in FreqCroiss:

		a, b = tuples 
		f.write(str(a) + " " + str(b) + "\n")

	return(FreqCroiss)






#derniere modif : changer FreqCroiss = str(sorted()) en FreqCroiss = sorted()