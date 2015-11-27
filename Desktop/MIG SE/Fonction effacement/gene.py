
def actualise_etat_et_gene(instance_machine, date):
    instance_machine.modifierEtatActuel( - 0.01 )
    instance_machine.modifierGene( 
            instance_machine.renvoyerGene() + get_delta_gene(instance_machine, date) 
            )
    
    
def get_delta_gene(instance_machine, date):
    if instance_machine.renvoyerNom() == "chauffage" or instance_machine.renvoyerNom() == "clim" :
        ea = instance_machine.renvoyerEtatActuel() #etat actuel (entre 0 et 1)
        cm = instance_machine.renvoyerConsoMax() #conso max, en W
        Pq_actuelle = ea*cm #conso actuelle, en W
        Pq_après = Pq_actuelle - 0.01*cm #0.01 pas d'état à fixer
        temp_actuelle = calcul_temp(Pq_actuelle)
        temp_apres = calcul_temp(Pq_apres)
        gene_apres = calcul_gene_t(temp_apres)
        delta_gene = gene_apres - instance_machine.renvoyerGene() 
        return( delta_gene )
    if instance_machine.renvoyerNom() == "lumiere" :
        if date.hour < 9 and date.hour > 19 :
            return()
        elif date.hour >=16 and date.hour <19 and date.month >=10 and date.month <=3 :
           return()
        else :
            return() #idem pour la lumière, gène arbitraire
    
    
        

def calcul_gene_t(x):   #calcul de la gene en fonction de T
    if instance_machine.renvoyerNom() == "chauffage" or instance_machine.renvoyerNom() == "clim" :
        if 19 <= x <= 25:
            return(((x-22)**4)/81)
        else:
            return(1)
    
        
def calcul_temp(p):
    return() #calcul de la température en fonction de la Puiss. Calorifique
    
    
    


    
    

        
            
        