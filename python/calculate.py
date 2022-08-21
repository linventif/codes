while True :
    
    premier_nombre = input("Veuillez entrer un premier nombre : ")
    deuxieme_nombre = input("Veuillez entrer un deuxième nombre : ")

    if premier_nombre.isdigit() and deuxieme_nombre.isdigit() :
        somme = (int(deuxieme_nombre) + int(premier_nombre))
        print(f"Le résultat de l'addition du nombre {premier_nombre} avec le nombre {deuxieme_nombre} est égal à {somme}.")
    else :
        print("Un des un nombres entrée n'est pas valide !") 