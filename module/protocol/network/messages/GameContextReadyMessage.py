from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameContextReadyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6225
        self.mapId = {"type": "Number", "value": ""}
