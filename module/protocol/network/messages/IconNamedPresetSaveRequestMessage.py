from module.protocol.network.messages.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


class IconNamedPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        IconPresetSaveRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9336
        self.name = {"type": "String", "value": ""}
        self.type = {"type": "uint", "value": ""}
