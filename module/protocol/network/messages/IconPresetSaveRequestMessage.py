from module.protocol.network.message import Message


class IconPresetSaveRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6308
        self.presetId = {"type": "int", "value": ""}
        self.symbolId = {"type": "uint", "value": ""}
        self.updateData = {"type": "Boolean", "value": ""}
