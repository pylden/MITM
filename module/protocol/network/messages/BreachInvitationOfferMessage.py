from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachInvitationOfferMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5041
        self.host = {"type": "CharacterMinimalInformations", "value": ""}
        self.timeLeftBeforeCancel = {"type": "uint", "value": ""}
