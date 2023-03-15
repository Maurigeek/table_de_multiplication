"""Ce programme affiche la table de multiplication de 0 à 12"""

print('\n')
print(" *|    0    1    2     3   4    5    6    7    8    9   10   11   12")
print("--+-----------------------------------------------------------------")

# Affichez chaque ligne de multiplication :
for number1 in range(13):
    # Affiche les étiquettes des numéros verticaux :
    # et la barre de séparation
    print("{}|".format(number1).rjust(3), end="")

    # Affiche le produit suivi d'un espace :
    for number2 in range(13):  
        print(" {}".format(number1 * number2).rjust(5), end="")
    print()
        
print("--+-----------------------------------------------------------------")   
print('\n')
    
    
