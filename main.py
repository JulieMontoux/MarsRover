from src.rover import Rover

def main():
    planete = (10, 10)
    obstacles = [(3, 3), (5, 5), (7, 7)]
    rover = Rover(5, 5, 'N', planete, obstacles)


    print("Aujourd'hui vous êtes au contrôle de Rover !")
    print("Commandes :")
    print(" - 'A' : avancer")
    print(" - 'R' : reculer")
    print(" - 'G' : tourner à gauche")
    print(" - 'D' : tourner à droite")
    print(" - 'Q' : quitter")

    while True:
        commande = input("Entrez une commande : ").upper()

        if commande in ['A', 'R']:
            rover.deplacer(commande)
        elif commande in ['G', 'D']:
            rover.tourner(commande)
        elif commande == 'S':
            sequence = input("Entrez une séquence de commandes : ").upper()
            rover.executer_commandes(sequence)
        elif commande == 'Q':
            print("On se revoit bientôt sur Mars !")
            break
        else:
            print("Commande invalide. Veuillez réessayer.")
            continue

        print(rover.get_position())

if __name__ == "__main__":
    main()
