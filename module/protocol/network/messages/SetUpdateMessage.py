from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SetUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1745
        self.setId = {"type": "uint", "value": ""}
        self.setObjects = {"type": "Vector.<uint>", "value": ""}
        self.setEffects = {"type": "Vector.<ObjectEffect>", "value": ""}
