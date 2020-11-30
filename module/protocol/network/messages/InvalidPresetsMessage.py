from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InvalidPresetsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2448
        self.presetIds = {"type": "Vector.<uint>", "value": ""}
