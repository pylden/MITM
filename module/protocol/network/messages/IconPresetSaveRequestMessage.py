from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IconPresetSaveRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6308
        self.presetId = {"type": "int", "value": ""}
        self.symbolId = {"type": "uint", "value": ""}
        self.updateData = {"type": "Boolean", "value": ""}
