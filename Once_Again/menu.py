def menu() -> dict:
    """Création du personnage : retourne le dictionnaire gameState."""
    print("Bienvenue dans ONCE AGAIN, ravi de vous rencontrer même si vous verrez bien vite que l'on s'est déjà croisés. N'est-ce pas ??")
    nom: str = input("Rafraichissez moi la mémoire, vous êtes ? ")
    gameState: dict = {
        "anti staminique": False,
        "jours": 3,
        "tuto": True,
        "nom": nom,
        "fatigue": 5,
        "poches": [],
        }
    print(f"A présent {nom}, vous vous sentez ainsi : \nFatigue : {gameState['fatigue']}, \nVous avez deux poches, elles sont vides.\n")
    return gameState
