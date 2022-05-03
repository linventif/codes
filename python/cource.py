import random
import time
import os

menu_commande = ["Ajouter un élément à la liste", "Retirer un élément à la liste", "Afficher la liste", "Vider la liste", "Quiter"]
liste_de_course = []

while True :

    os.system("clear")
    print("Choisissez parmi ces 5 commandes suivantes :")

    nombre = 1
    for element in menu_commande :
        print (f"{nombre}: {element}")
        nombre += 1

    reponse = input("Votre choix : ")

    if not reponse.isdigit() or ((int(reponse) > 5) or (int(reponse) < 0)) :
        os.system("clear")         
        print("---------------------------------------------------")
        print("------- Le nombre entrée n'est pas valide ! -------")
        print("---------------------------------------------------")
        time.sleep(1.5)
        os.system('cls||clear')
        continue
    
    reponse = int(reponse)

    if reponse == 1 :
        os.system('cls||clear')  
        reponse = input("Entrer le nom de votre nouvelle element : ")
        liste_de_course.append(reponse)
        os.system("clear")         
        print("---------------------------------------------------")
        print(f"L'élement {reponse} de à étais rajouter a votre liste !")
        print("---------------------------------------------------")
        time.sleep(1.5)
    
    if reponse == 2 :
        if not liste_de_course :
            os.system("clear")         
            print("---------------------------------------------------")
            print("------------- Votre liste est vide ! --------------")
            print("---------------------------------------------------")
            time.sleep(1.5)
            continue
        nombre = 1
        os.system("clear")
        print("Voici le contenu de votre liste : ")
        for element in liste_de_course :
            print (f"{nombre}. {element}")
            nombre += 1
        print("Quelle element voulez vous supprimer ?")
        reponse = input("Votre choix : ")
        while not reponse.isdigit() :
            nombre = 1
            os.system("clear")
            print("Voici le contenu de votre liste : ")
            for element in liste_de_course :
                print (f"{nombre}. {element}")
                nombre += 1
            print("Quelle element voulez vous supprimer ?")
            reponse = input("Votre choix : ")
        liste_de_course.pop(int(reponse) - 1)
        os.system("clear")         
        print("---------------------------------------------------")
        print(f"-- L'élement {int(reponse)} de votre liste à étais enlever !--")
        print("---------------------------------------------------")
        time.sleep(1.5)
        

    if reponse == 3 :
        if not liste_de_course :
            os.system("clear")         
            print("---------------------------------------------------")
            print("------------- Votre liste est vide ! --------------")
            print("---------------------------------------------------")
            time.sleep(1.5)
            continue
        nombre = 1
        os.system("clear")
        print("Voici le contenu de votre liste : ")
        for element in liste_de_course :
            print (f"{nombre}. {element}")
            nombre += 1
        print("Retournée au menu des commande ? (y/n)")
        reponse = input("Votre choix : ")
        while not reponse.isalpha() or (len(reponse) != 1) or (reponse != "y") :
            nombre = 1
            os.system("clear")
            print("Voici le contenu de votre liste : ")
            for element in liste_de_course :
                print (f"{nombre}. {element}")
                nombre += 1
            print("Retournée au menu des commande ? (y/n)")
            reponse = input("Votre choix : ")
            
    if reponse == 4 :
        if not liste_de_course :
            os.system("clear")         
            print("---------------------------------------------------")
            print("------------- Votre liste est vide ! --------------")
            print("---------------------------------------------------")
            time.sleep(1.5)
            continue
        del liste_de_course[:]
        os.system("clear")         
        print("---------------------------------------------------")
        print("----------- Votre liste à étais vider ! -----------")
        print("---------------------------------------------------")
        time.sleep(1.5)

    if reponse == 5 :
        break