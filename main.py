import fonctionnalite.arbre.fonction_arbre as fa 
import fonctionnalite.lexique.freqNEW as freq 
import fonctionnalite.codage.codage as co 


#on input le nom du fichier texte à tester
nomFichier = input("entrez le nom du fichier à tester :")

a = open("./txt/source/" + nomFichier + ".txt", "r").read()

#on calcule les occurences de chaque caractère
freqCroiss, lettres = freq.freq(a)

#on crée l'arbre, on obtient la racine root
root = fa.creerArbre(freqCroiss)

#on crée le dictionnaire codes
codes = co.encodage(root)

#on compresse le texte source
compressed = co.compression(codes, a)

#on calcule le taux de compression
taux = co.tauxCompression(a, compressed)
print("taux de compression : " + str(taux))

#on calcule le nb moyen de bits de stockage alloué à un caractère
nbmoyen = co.nbMoyen(codes)
print("nombre moyen : " + str(nbmoyen))






