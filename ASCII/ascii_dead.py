"""
Exemple de dessin ASCII simple.

Pour créer votre propre dessin :
  1. copiez ce fichier dans le dossier ASCII sous le nom ascii_quelquechose.py ;
  2. renommez la fonction ascii_quelquechose (même nom que le fichier) et
     gardez le typage : def ascii_quelquechose() -> None ;
  3. collez votre dessin entre les triple guillemets.

Le r placé juste avant les triple guillemets du print est important :
sans lui, Python interprète mal les barres obliques inversées du dessin.

Pour l'utiliser dans une page :
    from ASCII.ascii_dragon import ascii_dragon
    ascii_dragon()
"""


def ascii_dead() -> None:
    
    import os
    import time
    import random

    # Couleurs ANSI
    RESET = "\033[0m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    GRAY = "\033[90m"
    YELLOW = "\033[93m"

    def color(text, c):
        return c + text + RESET

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    # Tête du personnage
    head = [
        "             .-=========-.",
        "           .'             '.",
        "          /                 \\",
        "         /                   \\",
        "        |                     |",
        "        |     x         x     |",
        "        |                     |",
        "        |          ^          |",
        "        |       \\_____/       |",
        "         \\                   /",
        "          '.               .'",
        "            '-._________.-'"
    ]

    # Âme et nuage : plusieurs positions
    souls = [
    [
    " ",
    " ",
    " ",
    " ",
    ],
    [
    "             .-~~~~~-.",
    "          .-'         '-.",
    "         (    .---.      )",
    "          '-.( o o ).-'",
    ],
    [
    "                  .-~~~~~-.",
    "               .-'         '-.",
    "              (    .---.      )",
    "               '-.( o o ).-'",
    ],
    [
    "                        .-~~~~~-.",
    "                     .-'         '-.",
    "                    (    .---.      )",
    "                     '-.( o o ).-'",
    ],
    [
    "                              .-~~~~~-.",
    "                           .-'         '-.",
    "                          (    .---.      )",
    "                           '-.( o o ).-'",
    ],
    [
    "                                    .-~~~~~-.",
    "                                 .-'         '-.",
    "                                (    .---.      )",
    "                                 '-.( o o ).-'",
    ]
    ]

    # Petites particules
    particles = ["*", ".", "+", "·"]

    def draw(frame):
        clear()

        print()
        print(color("              G A M E   O V E R", RED))
        print(color("          Your soul has left your body...", PURPLE))
        print()

        # Affichage du nuage et de l'âme
        for line in souls[frame]:
            if line.strip():
                print(color(line, PURPLE))

        # Particules lumineuses
        for i in range(3):
            spaces = " " * random.randint(5, 30)
            particle = random.choice(particles)
            print(spaces + color(particle, CYAN))

        print()

        # Tête
        for i, line in enumerate(head):
            if i < 5:
                print(color(line, GRAY))
            elif i < 9:
                print(color(line, WHITE))
            else:
                print(color(line, GRAY))

        print()
        print(color("          Press any key to continue...", BLUE))

    # Animation
    try:
        while True:
            # Montée progressive de l'âme
            for frame in range(len(souls)):
                draw(frame)
                time.sleep(0.55)

            # L'âme disparaît dans le ciel
            for i in range(4):
                clear()
                print()
                print(color("              G A M E   O V E R", RED))
                print()

                for line in head:
                    print(color(line, GRAY))

                print()
                print(color("               The soul is gone.", PURPLE))
                time.sleep(0.4)

    except KeyboardInterrupt:
        clear()

