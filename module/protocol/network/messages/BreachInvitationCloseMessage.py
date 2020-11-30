from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachInvitationCloseMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 608
        self.host = {"type": "CharacterMinimalInformations", "value": ""}
