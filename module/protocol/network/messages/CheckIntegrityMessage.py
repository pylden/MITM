from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CheckIntegrityMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8606
        self.data = {"type": "Vector.<int>", "value": ""}
