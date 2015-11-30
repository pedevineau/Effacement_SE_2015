import analyseDonnees
import datetime
import Machine_verif as mv
import analyseDonnees as ad
dateTest = datetime(2015,5,1)


conso_Bouilleur = ad.renvoyerJourneeTypeAvecMax( "Bouilleur Friteuses Vaisselle.csv",origine_de_la_simulation )																													)
Bouilleur = mv.Machine( "Bouilleur", conso_Bouilleur[0], conso_Bouilleur[1]/conso_Bouilleur[0], 0.5, True, 0 )

conso_SplashBattle = ad.renvoyerJourneeTypeAvecMax( "Splash Battle.csv",origine_de_la_simulation )																													)
SplashBattle = mv.Machine( "Splash Battle", conso_SplashBattle[0], conso_SplashBattle[1]/conso_SplashBattle[0], 0.5, True, 0 )

conso_Creperie =ad.renvoyerJourneeTypeAvecMax( "Crèperie Gaufrier Rotisoire.csv",origine_de_la_simulation )
Creperie = mv.Machine( "Creperie", conso_Creperie[0], conso_Creperie[1]/conso_Creperie[0], 0.5, False, 0 )

conso_PCnormal =ad.renvoyerJourneeTypeAvecMax( "PCnormal.csv",origine_de_la_simulation )
PCnormal = mv.Machine( "PCnormal", conso_PCnormal[0], conso_PCnormal[1]/conso_PCnormal[0], 0.5, False, 0 )

print(PCnormal)
