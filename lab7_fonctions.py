def saluer():
    print("Bonjour depuis une fonction !")
    print("Ravi de te voir")
saluer()  

def presentation(nom, age):
    print(f"Je m'appelle {nom} et j'ai {age} ans")

presentation("Alice", 30)
presentation("Mohamed", 25)

def additionner(a, b):
    total = a + b
    print(total)
resultat = additionner(3, 5)
print("Résultat :", resultat)

type(additionner)

def calcul_ttc(prix_ht, taux=0.2):
    prix_ttc = prix_ht * (1 + taux)
    return prix_ttc

print(calcul_ttc(100))           
print(calcul_ttc(100, 0.055))   
print(calcul_ttc(prix_ht=50, taux=0.1)) 

print("\n")
def afficher_message(message, prefix="[INFO]"):
    print(f"{prefix} {message}")

afficher_message("Début du traitement.")
afficher_message("Fichier non trouvé", prefix="[ERREUR]")
afficher_message("Action réussie", prefix="[SUCCÈS]")
print("\n")

def somme(*args):
    total = 0
    for valeur in args:
        total += valeur
    return total

print(somme(1, 2))
print(somme(1, 2, 3, 4))


def produit(*args):
    if not args:
        return 1
    
    total = 1
    
    for valeur in args:
        total *= valeur 
        
    return total
print(f"Produit de (2, 3) : {produit(2, 3)}")       
print(f"Produit de (5, 2, 4) : {produit(5, 2, 4)}")  
print(f"Produit de () : {produit()}")              

