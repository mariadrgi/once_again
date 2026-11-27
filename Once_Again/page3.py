from ASCII.ascii_dead import ascii_dead
import time
def page3(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu

    print( " Tu sors de chez toi rapidement et démarres en trombe pour oser espérer arriver à l'heure au travail, mais tu es fatigué.e, si fatiguée..." )
    print (" Tu roules largement au-delà de la vitesse autorisée, mais tant pis !! Et ce camion, pourquoi ne reste-t-il pas dans sa voie ??")
    print( "Mais que faire , tu dois accélérer? ou freiner? pourquoi ne ralentit-il pas?..." )

    time.sleep(10)
    ascii_dead()
    res= 1 

    return res