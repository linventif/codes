from random import *
import time
import os

os.system("clear")   

nombre_de_tour = 0
point_de_vie = 50
point_de_vie_enemie = 50
nombre_de_potion = 3

while (point_de_vie > 1) and (point_de_vie_enemie > 1) :

    os.system("clear")  
        
    print(f"-------------------- Tour n°{nombre_de_tour} ---------------------")
    print("---------------------------------------------------")
    print(f"------ Vos points de vie : {str(point_de_vie).zfill(2)} ---------------------")
    print(f"------ Points de vie de l'enemie : {str(point_de_vie_enemie).zfill(2)} -------------")
    print(f"------ Nombre de potion restente : {str(nombre_de_potion).zfill(2)} -------------")
    print("---------------------------------------------------")
    print()
    print("------------ Choisiser une commande ---------------")
    print("---------------------------------------------------")
    print("------ 1: Attaquer l'ennemie ----------------------")
    print("------ 2: Prendre une potion ----------------------")
    print("---------------------------------------------------")
    print()

    reponse = input("Votre choix : ")

    if not reponse.isdigit() or ((int(reponse) > 2) or (int(reponse) < 1)) :
        os.system("clear")    
        print("---------------------------------------------------")
        print("------- Le nombre entrée n'est pas valide ! -------")
        print("---------------------------------------------------")
        time.sleep(1.5)
        os.system('cls||clear')
        continue

    reponse = int(reponse)

    if reponse == 1 :
        os.system("clear")   
        degat_infliger = randint(5, 10) 
        degat_reçu = randint(5, 15)   
        print("---------------------------------------------------")
        print("--------- Vous avez attaquer l'ennemie ! ----------")
        print("----------- L'ennemie vous a attaquer ! -----------")
        print("---------------------------------------------------")
        print(f"------ Dégat infliger {str(degat_infliger).zfill(2)} ---- Dégat reçus {str(degat_reçu).zfill(2)} ------")
        print("---------------------------------------------------")
        point_de_vie -= degat_reçu
        point_de_vie_enemie -= degat_infliger
        time.sleep(3.5)
        continue

    if reponse == 2 :
        if nombre_de_potion == 0 :
            os.system("clear")         
            print("---------------------------------------------------")
            print("--------- Vous n'avez plus de potions -------------")
            print("---------------------------------------------------")
            time.sleep(1.5)
            continue
        point_de_vie_gagnier = randint(15, 50)
        point_de_vie += point_de_vie_gagnier
        nombre_de_potion -= 1
        os.system("clear")         
        print("---------------------------------------------------")
        print("--------- Vous avez utuliser une potion ! ---------")
        print("---------------------------------------------------")
        print(f"------ Vous avez gagnier {point_de_vie_gagnier} points de vie ! -------")
        print("---------------------------------------------------")
        print(f"----------- Il vous reste {str(nombre_de_potion).zfill(2)} potions ! ------------")
        print("---------------------------------------------------")
        time.sleep(3.5)

        os.system("clear")   
        degat_reçu = randint(5, 15)   
        print("---------------------------------------------------")
        print("----------- L'ennemie vous a attaquer ! -----------")
        print("---------------------------------------------------")
        print(f"----------------- Dégat reçus {str(degat_reçu).zfill(2)} -----------------")
        print("---------------------------------------------------")
        point_de_vie -= degat_reçu
        time.sleep(3.5)
        continue

os.system("clear")   

if point_de_vie >= point_de_vie_enemie :
    print("---------------------------------------------------")
    print("----------- Vous avez gagnier le combat -----------")
    print("---------------------------------------------------")
else :
    print("---------------------------------------------------")
    print("------------ Vous avez perdu le combat ------------")
    print("---------------------------------------------------")
