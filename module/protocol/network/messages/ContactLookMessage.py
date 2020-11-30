from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ContactLookMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6821
        self.requestId = {"type": "uint", "value": ""}
        self.playerName = {"type": "String", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.look = {"type": "EntityLook", "value": ""}
