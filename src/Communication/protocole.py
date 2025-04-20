class ProtocoleCommunication:
    COMMANDES_VALIDES = {'A', 'R', 'G', 'D'}

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
        return f"📡 Réponse du rover : {contenu}"