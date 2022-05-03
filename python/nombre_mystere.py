from math import isfinite
from random import *

myster_number = randint(1, 100)
essais = 5

print("*** Le jeu du Nombre Mystère *** ")

while (essais > 0) or (reponse == myster_number) :
    print(f"Il te reste {essais} essais !")

    reponse = input("Devine le nombre : ")

    while not reponse.isdigit() :
        print("Le nombre entrée n'est pas valide !")
        reponse = input("Devine le nombre : ")
        
    reponse = int(reponse)

    if reponse < myster_number :
        grandeur = "grand"
    elif reponse > myster_number :
        grandeur = "petit"
    elif reponse == myster_number :
        print(f"Bravo ! Le nombre mystère était bien {myster_number}.")
        print(f"Tu as trouvé le nombre en {5 - essais } essais.") 
        break

    print(f"Le nombre mytère est plus {grandeur} que {reponse}.")
    
    essais -= 1       

if reponse != myster_number :
    print(f"Domage ! Le nombre mystère était {myster_number}.")

print("Fin du jeu.")