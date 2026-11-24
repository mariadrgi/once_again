def page1(gameState: dict) -> int:
    res: int = -2                     # par défaut : cas non prévu
    

    print("Tu ouvcres les yeux, tu as froid, le frigo fait du bruit, il y a du brouillard dehors, il fait noir. Tu regardes l'heure : il est 6h06, sans savoir pourquoi, tu es envahi par un mauvais présentiment")
    print(f"Fatigue : {gameState['fatigue']}" )
    print("Sur votre table de chevet, des cachets, 1) bleus  et 2) verts")
    choix: str = input("Choix : ")

    if choix == "1":
        gameState["fatigue"]=gameState["fatigue"]-3
        print(f"Votre fatigue diminue progressivement jusque {gameState['fatigue']}.")
    elif choix == "2":
        gameState["fatigue"]=gameState["fatigue"]+2
        print(f"Votre fatigue augmente brutalement jusque {gameState['fatigue']}.")
    else:
        print("Choix invalide.")
        res = 1     
    
    print("Que fais-tu ?")     
    print("1--Tu te recouches 5 minutes, que cela va-t-il bien changer…") 
    print("2--5 appels manqués de Papa. Depuis quand a-t-il décidé de prendre des nouvelles ? Tu le rappelles…")
    print("De toute façon, pas le choix. Tu te prépares et prends la route du travail comme d'habitude…")  
    choix_2: str = input("Choix : ")

    if choix_2=="1":
        res = 2
    elif choix_2=="2":
        res = 3
    elif choix_2=="3":
        res = 4
    else: 
         res = 1
         print("Choix invalide")

    return res
