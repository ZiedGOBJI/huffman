#obtenir le code de chaque caractère individuellement
def encodage(node, chemin = ""):

	codes = {}

	if node.isFeuille():
		if chemin == "":
			codes[node.getLabel()] = "0"
		else:
			codes[node.getLabel()]=chemin 	
		return codes 


	else:

		codes.update(encodage(node.getrightChild(), chemin+"1"))

		codes.update(encodage(node.getleftChild(), chemin+"0"))
		
		return codes

#on met bout à bout le code de chaque caractère du texte source pour obtenir le code du texte, et donc le texte compressé 
def compression(codes, texteSource):
	
	compressedText = ""

	for lettre in texteSource:

		compressedText += codes[lettre]

	f = open("./txt/resultat/compression.txt", "w")
	f.write(compressedText)

	return(compressedText)



#calcul du taux de compression
def tauxCompression(texteSource, compressedText):


#calcul volume initial (en octet)

	nbbitsSource = len(texteSource)*8
	nboctetsSource = nbbitsSource/8

#calcul volume final (en octet)

	nbbitsCompressed = len(compressedText)
	nboctetsCompressed = nbbitsCompressed/8

#calcul 1 - volume final/volume initial

	return 1-(nboctetsCompressed/nboctetsSource)


#calcul du nombre moyen de bits de stockage d'un caractère du texte compressé
def nbMoyen(codes):

	somme = 0

	for lettre in codes.values():
		somme += len(lettre)

	return(somme/len(codes))




	 