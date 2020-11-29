from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PresetDeleteRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7425
        self.vars.append({"name": "presetId", "type": "int", "value": ""})
