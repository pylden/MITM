from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PresetSaveErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8976
        self.vars.append({"name": "presetId", "type": "int", "value": ""})
        self.vars.append({"name": "code", "type": "uint", "value": ""})
