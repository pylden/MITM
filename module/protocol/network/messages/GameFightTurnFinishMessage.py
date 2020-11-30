from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnFinishMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 385
        self.isAfk = {"type": "Boolean", "value": ""}
