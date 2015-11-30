#   Retour typique du programme effacement_main, pour l'équipe affichage. 
# 
#  Plage de dates : le 2 mai 2015, 14:00 à 15:00, du fichier antibes/direction_architecture_batiments/Temperatures, T° Service Régie. 
#   Nombre de machines instanciées: 5 - lumière, chauffage, clim, et 1 à état discret.)

from datetime import *
import Machine_verif 
from random import *

def Matrice_test():
    liste_dates = [ datetime(2015, 5, 2, 14) + timedelta(seconds = i*600) for i in range(7) ]
    liste_temperatures = [ 23.64, 23.20, 22.51, 21.84, 21.20, 20.72, 20.48 ]
    matrice=[]    
    Clim = Machine_verif.Machine("Clim",100,0.7,0.85,1,0.1)
    Chauffage = Machine_verif.Machine("Chauffage",1200,0.37,0.99,1,0.3)
    Lampe = Machine_verif.Machine("Lampe",60,1,0.2,0,0.18)
    Friteuse = Machine_verif.Machine("Friteuse",1000,1,1,0,0.95)
    liste_machine = [Clim,Chauffage,Lampe,Friteuse]
    for nb_iter in range(7):
        for (k,machine) in enumerate(liste_machine):
            matrice[nb_iter][k]= [ machine.renvoyerNom(), machine.renvoyerEtatActuel(), machine.consoMachine(), machine.renvoyerGene() ]
            machine.modifierEtatActuel(random.random())
            x = random.random())            
            if 0 <= x <= 1:
                    machine.modifierGene(x)) 
            else:               
                machine.modifierGene(0.47) 
    return(liste_dates, liste_temperatures, matrice)