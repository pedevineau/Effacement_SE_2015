import pandas as pd
from datetime import *
import Machine_verif 
import Batiment_verif 
import Gene_verif as 
import datetime_to_temp_verif as dt

## déboguer les fonctions appelées
## fournir matrice exemple à l'équipe affichage

def datetime_to_temperature(datetime1):
    str1 = str(datetime1.day) + '/' + str(datetime1.month) + '/' +str(datetime1.year) + ' '             +str(datetime1.hour) + ':' +str(datetime1.minute) + ":" + str(datetime1.second)
    Data_frame_temperature =    pd.read_csv(Fichier,sep = ";",names=["date et heure","lieu","type1","type2","valeur","unité"],header=None)
    if str1 in Data_frame_temperature["date et heure"]:
        k = Data_frame_temperature["date et heure"].index(str1)
        return(Data_frame_temperature["valeur"][k])
    else:
        return("Date et heure non compatibles") ##path à régler selon l'ordi
        

def effacement_main( date_debut, Puissance_a_effacer ):

    ##instancier: liste_machines

#Objets return
    liste_dates = [ date_debut + timedelta(seconds = i*600) for i in range(7) ]
    liste_temp_int_simul = []*7
    #Initialisation de la matrice renvoyée, à l'état initial
    matrice = [][[]]
    for i,mac in enumerate(liste_machines):
        matrice[0][i]=[ mac.renvoyerNom(), mac.renvoyerEtatActuel(), mac.consoMachine(), mac.renvoyerGene() ] 
        

    Puissance_effacee = 0   
    liste_temp_int_simul[0] = [datetime_to_temperature(date_debut)]
    plus_modifiables = [machine for machine in liste_machines if machine.renvoyerEtatActuel() == 0]
    nb_iter = 0
    
    
    #Début de l'algorithme
    while Puissance_effacee < Puissance_a_effacer and len(plus_modifiables) != len(liste_machines):
        
        liste_tuples = []  
        for machine in liste_machines:
            if not (machine in plus_modifiables):
                if machine.renvoyerGene() >= 0.95:
                    liste_tuples.append( (0, machine) )
                    plus_modifiables.append(machine)
                elif machine.renvoyerEtatContinu():
                    if machine.renvoyerEtat() >= 0.01:
                        deltagene = get_delta_gene(machine, date_debut)
                        priorite = machine.consoMachine()/(deltagene*100)
                        liste_tuples.append( (priorite, machine) )
                    else:
                        liste_tuples.append( (0, machine) )
                        machine.modifierEtat( 0 )
                        plus_modifiables.append(machine)
                else:
                    priorite = machine.renvoyerConsoMax()/machine.renvoyerGene() 
                    liste_tuples.append( (priorite, machine) )
                    plus_modifiables.append(machine)
            else:
                liste_tuples.append( (0, machine) )
                       
        liste_tuples_sorted = sorted(liste_tuples, reverse = True)
        machine_prior = liste_tuples_sorted[0](1)
        if not ( len(plus_modifiables) == len(liste_machines) and machine_prior.renvoyerEtatContinu() ):
            Puissance_effacee += machine_prior.renvoyerConso()
            machine_prior.actualise_etat_et_gene(machine, date_debut)
        for k, mach in enumerate( liste_tuples_sorted ):
            matrice[nb_iter][k]=[ mach.renvoyerNom(), mach.renvoyerEtatActuel(), mach.consoMachine(), mach.renvoyerGene() ]
        nb_iter += 1
        
        
    #Début de la boucle temporelle:
    for date in liste_dates[1::]:
        Puissance_tot = sum( [matrice[nb_iter][x][2] for x in range( len(liste_machines) ) ])
        liste_temp_int_simul.append( calcul_temp(Puissance_tot) ) 
        ##fonction calcul_temp à définir en fonction de P_tot, T_préc, T_ext(date)
    
    #retour de la liste des temps, liste temporelle des températures simulées, et la matrice pas à pas
    return(liste_dates, liste_temp_int_simul, matrice)
        
        
        
            
                
                
                
    
    




