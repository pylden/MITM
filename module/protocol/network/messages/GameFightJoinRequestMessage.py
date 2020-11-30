from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightJoinRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3211
        self.fighterId = {"type": "Number", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
