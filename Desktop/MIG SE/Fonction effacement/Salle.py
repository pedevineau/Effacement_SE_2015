class Salle : 

	def __init__(self, nom, machines) : 
		self.__nomSalle = nom
		self.__machinesSalle = machines

	def consoSalle(self):
		conso = 0
		for machine in self.__machinesSalle : 
			conso += machine.consoMachine()
		return conso


	def ajouterMachine(self, machine) : 
		self.__machinesSalle.append(machine)

	def effacement(self, puissAEconomiser) : ###à modifier
		for machine in self.machinesSalle :
			machine.changeEtat(0)

	def renvoyerMachines(self) : 
		return machinesSalle

	def __str__(self) : 
		s = self.__nomSalle + " contient : \n"
		for machine in self.__machinesSalle : 
			s += "\t\t"
			s += str(machine)
			s += "\n"
		return s
#||||||||||||||||||||||||  DONNE  |||||||||||||||||||||||||||||||||||||||||||
	def renvoyerNom (self) :
		return self.__nomSalle
	def renvoyerMachines(self) :
		return self.__machines


#||||||||||||||||||||||||  MODIFIER  ||||||||||||||||||||||||||||||||||||||||

#Normalement pas besoin de medodes modifier

#||||||||||||||||||||||||  METHODES  ||||||||||||||||||||||||||||||||||||||||

	def rechercherMachine (self, nom) :
		for m in self.__machinesSalle :
			if ( m.renvoyerNom() == nom ) :
				return m
		return None


	
