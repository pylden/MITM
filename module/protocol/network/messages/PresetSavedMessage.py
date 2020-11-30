from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PresetSavedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4545
        self.presetId = {"type": "int", "value": ""}
        self.preset = {"type": "Preset", "value": ""}
