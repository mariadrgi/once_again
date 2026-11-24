def page6(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu
    essais : int= 0 
    secret : int= 
    trouve : bool= False

    print (" Les 5 appels en absence te préoccupent énormément...")
    print (" Tu remarques que suite à une mise à jour, ton téléphone te redemande d'entrer ton code PIN... Pourquoi fallait-il que ca tombe aujourd'hui??")
    print (" Mais... Quel est ton code PIN, déjà ?? 1234? Non, trop simple... Arghhhh !!!")
    print (" Tu sais seulement qu'il est en lien avec ... Mais attention, au bout de 3 tentatives, le téléphone est bloqué !")

    mdp : str = input ( "Code PIN : ")
    while essais< 3 and not trouve :
        essais +=1 
        print ( "PIN erroné")
        if mdp == secret:
            trouve=True
            

    if trouve=True :
        res= 7
    else :
        res= 11 

    return res 
