from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PresetSaveErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8976
        self.presetId = {"type": "int", "value": ""}
        self.code = {"type": "uint", "value": ""}
