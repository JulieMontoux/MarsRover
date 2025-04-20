
#Gère l'interprétation des messages reçus et la génération des réponses.
class ProtocoleCommunication:

    COMMANDES_VALIDES = {'A', 'R', 'G', 'D'}
    #Analyse un message reçu du client et Renvoie un tuple (type_commande, contenu).
    @staticmethod
    def parser_message(message):
        message = message.strip().upper()

        if message == "POSITION":
            return ("position", None)
        elif set(message).issubset(ProtocoleCommunication.COMMANDES_VALIDES):
            return ("mouvement", message)
        else:
            return ("invalide", message)

    @staticmethod
    def formater_reponse(contenu):
        """
        Formate une réponse lisible pour le client.
        """
        return f"📡 Réponse du rover : {contenu}"
