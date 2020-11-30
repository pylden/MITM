from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PresetsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1558
        self.presets = {"type": "Vector.<Preset>", "value": ""}
