from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameMapNoMovementMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6980
        self.cellX = {"type": "int", "value": ""}
        self.cellY = {"type": "int", "value": ""}
