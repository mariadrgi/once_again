def page1(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu
    
    if gameState["tuto"] == True :
        print("Tu ouvres les yeux, tu as froid, le frigo fait du bruit, il y a du brouillard dehors, il fait noir. Tu regardes l'heure : il est 6h06, sans savoir pourquoi, tu es envahi par un mauvais présentiment...")
        print(f"Fatigue : {gameState['fatigue']}" )
        print("Sur votre table de chevet, des cachets, 1) bleus et 2) verts. \nL'un réduit votre fatigue et l'autre est votre dernier cachet d'anti staminique")
        
        choix: str = input("Choix : ")

        print("Vous en verrez les effets dans quelques secondes... \n Voulez vous 1) aller au travail coûte que coûte ? Ou 2) prendre deux secondes de plus pour chercher un trucs à manger...")
        
        if choix == "1":
            res = 3
            gameState["tuto"] = False
        elif choix == "2":
            res = 4
            gameState["tuto"] = False
        else:
            print("Choix invalide.")
            res = 1  
    
    else :
        print("Tu ouvres les yeux, tu as froid, le frigo fait du bruit, il y a du brouillard dehors, il fait noir. Tu regardes l'heure : il est 6h06, sans savoir pourquoi, tu es envahi par un mauvais présentiment")
        print("Tu as surement fait un mauvais rêve... Que fais-tu ?")  
        print("Sur votre table de chevet, des cachets, 1) votre anti-staminique et 2) vos vitamine. \nL'un réduit votre fatigue et l'autre est votre dernier cachet d'anti staminique")

        choix: str = input("Choix : ")
        if choix== "1":
            print("Maladroit comme vous êtes, vous le faite tomber sous votre lit !!!")
            print("Il vous reste toujours celui qui réduit la fatigue.. Glup.. Les effets commencent déjà")
            gameState["fatigue"] += 2
            print(f"Fatigue : {gameState["fatigue"]}")
        print("1--Tu te recouches 5 minutes, que cela va-t-il bien changer…") 
        print("2--Tu voies que tu as 5 appels manqués de Papa sur ton pc. Depuis quand a-t-il décidé de prendre des nouvelles ? Tu le rappelles…")
     
        choix_2: str = input("Choix : ")

        if choix_2=="1":
            res = 5
        elif choix_2=="2":
            res = 6
        else: 
            res = 1
            print("Choix invalide")

    return res
