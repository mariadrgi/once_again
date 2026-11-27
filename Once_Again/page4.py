from ASCII.ascii_dead import ascii_dead
import time

def page4(gameState: dict) -> int:
    res: int = -2  # par défaut : cas non prévu

    print(
        "Tu as faim, si faim... Oh ! Une barre de céréales est posée sur le "
        "comptoir de la cuisine. Tu la manges à cœur joie, juste pour réaliser "
        "qu'elle contient... des cacahuètes !!"
    )
    time.sleep(7)
    print(
        "Tu sens ta gorge gonfler, l'air commence à te manquer... Mais, "
        "normalement tu avais pris tes antistaminiques ce matin... À moins que "
        "tu te sois trompé de boîte de cachets ??!"
    )
    time.sleep(7)
    ascii_dead()
    res = 1
    return res