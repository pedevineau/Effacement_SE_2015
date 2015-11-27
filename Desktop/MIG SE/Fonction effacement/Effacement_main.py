

def effacement_glouton( date_debut, date_fin, Puissance_a_effacer ): 
    jour_debut = int(date_debut[0:2])   
    mois_debut = int(date_debut[3:5])
    annee_debut = int(date_debut[6:10])    
    heure_debut = int(date_debut[11:13])  
    min_debut = int(date_debut[14:16])    
    sec_debut = int(date_debut[17:19])  
    jour_fin = int(date_fin[0:2]) 
    mois_fin = int(date_fin[3:5])   
    annee_fin = int(date_fin[6:10])   
    heure_fin = int(date_fin[11:13])  
    min_fin = int(date_fin[14:16]) 
    sec_fin = int(date_fin[17:19])
    
    Puissance_effacee = 0   
    liste_tuples = []    
    Puiss = Puissance_a_effacer    
    eteints = [machine for machine in liste_machine if machine.etat == 0]
    liste_consommation = []
    Donnees_etats = pd.DataFrame([])     
    
    date_actuelle = date_debut
    while date_actuelle < date_fin:
        while Puissance_effacee < Puiss and len(eteints)!=len(liste_machines):
            liste_delta_gene=np.asarray([get_delta_gene(machine, date) for machine in liste_machines])  
            liste_tuples = []
            for k in range(len(liste_machine)):
                if not(liste_machine[k] in eteints):
                    if liste_delta_gene[k] != 0:
                        liste_tuples.append((liste_machine[k].renvoyerConsoMax()/(100*liste_delta_gene[k]),liste_machine[k]))
                    else:
                        liste_tuples.append((float('inf'),liste_machine[k]))
            liste_tuples_sorted = sorted(liste_tuples, reverse = True)
            machine = liste_tuples_sorted[0](1)     
            if machine.renvoyerEtatContinu():
                if machine.renvoyerEtatActuel() > 0.01:
                    machine.modifierEtatActuel( machine.renvoyerEtatActuel() - 0.01 )
                    Puiss_effacee += 0.01*machine.renvoyerConsoMax()
                elif machine.renvoyerEtatActuel() == 0.01:
                    machine.modifierEtatActuel( machine.renvoyerEtatActuel() - 0.01 )
                    Puiss_effacee += 0.01*machine.renvoyerConsoMax()
                    eteints.append(machine) 
            else:
                machine.modifierEtatActuel( 0 ) 
                Puiss_effacee += machine.renvoyerConsoMax()
                eteints.append(machine)
            liste_temperature.append(temp_actuelle) #temp actuelle à definir
            argent_economie += 0 #a calculer
            Donnees_etats['k'] = [machine.etat for machine in liste_machines]
            liste_consommation.append(sum(machine.etat*machine.consommation for machine in liste_machine))
            Temps_ecoule + 600
            Donnees_renvoyees = pd.DataFrame(liste_temperature,liste_consommation, index = ['Temperature de la pièce','Consommation (W)'])
    return(Donnees_renvoyees,Donnees_etats)
    

def effacement_main( date_debut, date_fin, Puissance_a_effacer ):

##instancier les machines
##creer liste dates

#####################################################

##