import fonctionnalite.arbre.fonction_arbre as fa 
import fonctionnalite.lexique.freqNEW as freq 
import fonctionnalite.codage.codage as co 



nomFichier = input("entrez le nom du fichier à tester :")

a = open("./txt/source/" + nomFichier + ".txt", "r").read()

FreqCroiss, lettres = freq.freq(a)


root = fa.creer_arbre(FreqCroiss)

codes = co.encodage(root)

compressed = co.compression(codes, a)

taux = co.taux_compression(a, compressed)

print(co.nb_moyen(codes))






