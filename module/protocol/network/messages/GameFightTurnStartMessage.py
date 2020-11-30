from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnStartMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9429
        self.id = {"type": "Number", "value": ""}
        self.waitTime = {"type": "uint", "value": ""}
