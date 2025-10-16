heure_debut = int(input('Heure de début de la surveillance : '))
heure_fin = int(input('Heure de fin de la surveillance : '))
nbre_total_personnes = int(input('Nombre total de personnes : '))
list_heure_dentree = input('entrée les heures d\'entrée des personnes : ').split()B


for i in range(len(list_heure_dentree)):
    compteur = 0
    if list_heure_dentree[i] in range(heure_debut, heure_fin):
        compteur += 1
       
    print(compteur)

print("le nombre d'espions est : ", compteur)



