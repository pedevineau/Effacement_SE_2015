
class Batiment:
    
	def __init__(self, nom, salles) :
		self.__salles = salles #sous forme de liste
		self.__nom = nom

        
	def ajouterSalle(self, salle) :
		self.__salles.append(salle)
        
    
	def effacement(self, puissAEconomiser): ###à modifier
		for i in self.__salles:
			i.effacement(puissAEconomiser)
            
            
	def consoTotal(self):
		c = 0
		for i in self.__salles:
			c += i.consoSalle()
		return c
	   

	def __str__(self):
		s=""
		for i in self.__salles:
			s += "\t"
			s += i.__str__()+"\n"
		return self.__nom+" contient les salles suivantes :\n"+s

#||||||||||||||||||||||| DONNE  |||||||||||||||||||||||||||||||||||||||||||||||||

	def renvoyerSalles(self) :
		return self.__salles

	def renvoyeNom(self) :
		return self.__nom

def test_rallumage():
	for k in liste_machine:
		k.etat = 1

def Puiss_max_effaçable():
	Puiss_effaçable = 0
	for k in liste_machine:
		k.etat = 0
		if gene(k) > k.gene_max:
			k.etat = 1
		else:
			Puiss_effaçable+= k.consommation
    
##_______________________________________________________________________________






