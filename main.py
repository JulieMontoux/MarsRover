from rover import Rover

def main():
    planete = (10, 10)
    rover = Rover(5, 5, 'N', planete)

    print("Aujourd'hui vous êtes au contrôle de Rover !")
    print("Commandes :")
    print(" - 'A' : avancer")
    print(" - 'R' : reculer")
    print(" - 'G' : tourner à gauche")
    print(" - 'D' : tourner à droite")
    print(" - 'Q' : quitter")

    while True:
        commande = input("Entrez une commande : ").upper()

        if commande == 'A':
            rover.avancer()
        elif commande == 'R':
            rover.reculer()
        elif commande == 'G':
            rover.tourner_a_gauche()
        elif commande == 'D':
            rover.tourner_a_droite()
        elif commande == 'Q':
            print("Au bientôt sur mars !")
            break
        else:
            print("Commande invalide. Réessayer.")
            continue

        print(rover.get_position())

if __name__ == "__main__":
    main()
