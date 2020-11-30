from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DungeonKeyRingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6151
        self.availables = {"type": "Vector.<uint>", "value": ""}
        self.unavailables = {"type": "Vector.<uint>", "value": ""}
