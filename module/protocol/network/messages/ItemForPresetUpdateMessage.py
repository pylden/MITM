from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ItemForPresetUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8924
        self.presetId = {"type": "int", "value": ""}
        self.presetItem = {"type": "ItemForPreset", "value": ""}
