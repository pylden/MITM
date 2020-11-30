from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameContextRemoveElementMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 52
        self.id = {"type": "Number", "value": ""}
