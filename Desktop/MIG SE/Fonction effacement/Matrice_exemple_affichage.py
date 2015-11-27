#   Retour typique du programme effacement_main, pour l'équipe affichage. 
#
#   Plage de dates : le 2 mai 2015, 14:00 à 15:00, du fichier antibes/direction_architecture_batiments/Temperatures, T° Service Régie. 
#   Nombre de machines instanciées: 5 - lumière, chauffage, clim, et 2 à état discret.

from datetime import *

liste_dates = [ datetime(2015, 5, 2, 14) + timedelta(seconds = i*600) for i in range(7) ]
liste_temperatures = [ 23.64, 23.20, 22.51, 21.84, 21.20, 20.72, 20.48 ]
matrice=[][[]]
