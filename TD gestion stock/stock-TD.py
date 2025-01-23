import csv

stock={}

# Charger les données du fichier CSV dans le dictionnaire 'stock'
with open("stock.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stock[row["marchandise"]]=int(row["quantite"])

## sert à insérer 100 lignes pour avoir un affichage correct (on simule l'effacement de l'écran)
def cls():
    print ("\n" * 100)

# Fonction pour rechercher le stock d'une marchandise
def recherche(stock):
    cls()
    marchandise = input("Entrez le nom de la marchandise à rechercher : ")
    if  marchandise in stock:
        print(marchandise,"est dans le stock avec ",(row["quantite"]),"d'unité")
    else:
        print(marchandise,"n'est pas en stock")
    input("Appuyez sur Entrée pour continuer")



# Fonction pour mettre à jour le stock d'une marchandise
def maj(stock):
    cls()
    marchandise = input("Entrez le nom de la marchandise à mettre à jour : ")
    if marchandise in stock:
        quantite = int(input("Entrez la nouvelle quantité en stock : "))
        stock[marchandise] = quantite
        print(marchandise,"à était mis à jour à tant",quantite,"d'unité")
    else:
        print(marchandise,"n'existe pas dans les stock")
    input("Appuyez sur Entrée pour continuer")



# Fonction pour créer une marchandise
def creer(stock):
    cls()
    marchandise = input("Entrez le nom de la nouvelle marchandise : ")
    quantite = int(input("Entrez la quantité en stock : "))
    stock[marchandise] = quantite
    print("La nouvelle marchandise",marchandise,"a été ajoutée avec",quantite,"unités en stock.")
    input("Appuyez sur Entrée pour continuer")


# Fonction pour supprimer une marchandise
def supprime(stock):
    cls()
    marchandise = input("Entrez le nom de la marchandise à supprimer : ")
    if marchandise in stock:
        del stock[marchandise]
        print("La marchandise",marchandise,"a été supprimée du stock.")
    else:
        print("La marchandise" ,marchandise, "n'existe pas dans le stock.")
    input("Appuyez sur Entrée pour continuer")

# Fonction pour sauvegarder le stock dans le fichier CSV
def sauvegarde(stock):
    with open("stock.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(("marchandise","quantite"))  ## ecriture de l'en-tête des colonnes
        for valeur in stock:
            writer.writerow((valeur,stock[valeur]))  ## ecriture des marchandise et quantités


continu=True    ## booléen qui permettra d'arrêter le programme
cls()
while continu:
      ## affichage d'un menu
    print("taper 0 pour voir l'état du stock")
    print("taper 1 pour rechercher le stock d'une marchandise")
    print("taper 2 pour mettre à jour le stock d'une marchandise")
    print("taper 3 pour créer une marchandise")
    print("taper 4 pour supprimer une marchandise")
    print("taper 5 pour arrêter")
    choix=(input("quel est votre choix ?"))
    if choix=="0" or choix=="1" or choix=="2" or choix=="3" or choix=="4" or choix=="5":
        print()
        if choix=="0":
            cls()
            print(stock)
            print()
        if choix=="1":
            recherche(stock)
            print()
        if choix=="2":
            maj(stock)
            print()
        if choix=="3":
            creer(stock)
            print()
        if choix=="4":
            supprime(stock)
            print()
        if choix=="5":
            sauvegarde(stock)
            continu=False
            print("Au revoir")
    else:
        cls()

