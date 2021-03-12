#obtenir le code de chaque caractère individuellement

def encodage(node, chemin = ""):

	codes = {}

	if node.is_feuille():
		if chemin == "":
			codes[node.get_label()] = "0"
		else:
			codes[node.get_label()]=chemin 	
		return codes 


	else:

		codes.update(encodage(node.get_rightChild(), chemin+"1"))

		codes.update(encodage(node.get_leftChild(), chemin+"0"))
		
		return codes


def compression(codes, texte_source):
	
	compressed_text = ""

	for lettre in texte_source:

		compressed_text += codes[lettre]

	f = open("./txt/resultat/compression.txt", "w")
	f.write(compressed_text)

	return(compressed_text)




def taux_compression(texte_source, compressed_text):


#calcul volume initial (en octet)

	nb_bits_source = len(texte_source)*8
	nb_octets_source = nb_bits_source/8

#calcul volume final (en octet)

	nb_bits_compressed = len(compressed_text)
	nb_octets_compressed = nb_bits_compressed/8

#calcul 1 - volume final/volume initial

	return 1-(nb_octets_compressed/nb_octets_source)


def nb_moyen(codes):

#calcul somme des chemins de toutes les lettres de codes
	somme = 0

	for lettre in codes.values():
		somme += len(lettre)

	return(somme/len(codes))




	 