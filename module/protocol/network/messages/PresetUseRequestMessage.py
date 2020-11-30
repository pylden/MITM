from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PresetUseRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3898
        self.presetId = {"type": "int", "value": ""}
