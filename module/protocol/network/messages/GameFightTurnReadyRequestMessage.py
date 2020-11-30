from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnReadyRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9704
        self.id = {"type": "Number", "value": ""}
