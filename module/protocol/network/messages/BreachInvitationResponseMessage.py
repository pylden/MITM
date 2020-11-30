from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachInvitationResponseMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7771
        self.guest = {"type": "CharacterMinimalInformations", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
