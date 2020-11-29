from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PresetSavedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4545
        self.vars.append({"name": "presetId", "type": "int", "value": ""})
        self.vars.append({"name": "preset", "type": "Preset", "value": ""})
