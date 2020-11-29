from module.protocol.network.messages.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


class IconNamedPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        IconPresetSaveRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9336
        self.vars.append({"name": "name", "type": "String", "value": ""})
        self.vars.append({"name": "type", "type": "uint", "value": ""})
