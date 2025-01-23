Fini=False      # servira à déterminer que la partie à gagnée et que le programme doit se terminer
Cinq=False      # servira à déterminer l'arrêt de la génératio des nombres
Compteur=0     # nombre de coups
Trouve=5
from random import*

grille=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],]     # grille du jeu initiale
dejajoue=[[8,8,8,8,8],[8,8,8,8,8],[8,8,8,8,8],[8,8,8,8,8],[8,8,8,8,8],]

while Cinq==False:      # test de la génération des 5 chiffres
    ligne = randint(0,4)     # un numéro  aléatoire pour la ligne
    colonne= randint(0,4)     #numéro aléatoire pour la colonne
    grille[ligne][colonne]=1      # valeur 1 dans la grille en position aléatoire
    nombre=0
    for ligne1 in range(0,5):
        for colonne1 in range(0,5):
            if grille[ligne1][colonne1]==1:
                nombre=nombre+1
    if nombre==5:
        Cinq=True

for tew in dejajoue:         # affichage des ligne de DéjaJoué
    print(tew)
print()

while Trouve!=0 and Fini==False:      # tant que tout les bateau son pas trouver partie continue
    CoupValable=False
    while CoupValable==False:       # vérification que la case n'est pas déja jouée
        ligne=int(input("saisir un numéro de ligne entre 0 et 4,numéro de ligne rentré:"))
        colonne=int(input("saisir un numéro de colonne entre 0 et 4 ,numéro de colonne rentré:"))
        if(ligne<0 or ligne>4)or(colonne<0 or colonne>4)or dejajoue[ligne][colonne]!=8:       # test de la validité des données
             if(ligne<0 or ligne>4):
                print("Ligne hors bornes !! Veillez recommencer")
             else:
                if colonne<0 or colonne>4:
                    print("Colonne hors bornes !! Veillez recommencer")
                else:
                    if  dejajoue[ligne][colonne]!=8:
                        print("Case déjà jouée !! Veillez recommencer")
        else:
            CoupValable=True
            Compteur=Compteur+1     # rajoute un coup au compteur
            if grille[ligne][colonne]==1:     # dire : cible touchée
                dejajoue[ligne][colonne]=1
                Trouve=Trouve-1
                print("trouver")
            dejajoue[ligne][colonne]=grille[ligne][colonne]

        for tew in dejajoue:        # affiche les lignes de DéjaJoué
            print(tew)
        print()
    if Trouve==0:       #joueur à trouvé les cases
        Fini=True
if Fini==True:      # affiche fin de la partie
    print("Bravo vous avez trouvé tous les objets en",Compteur,"coups!")