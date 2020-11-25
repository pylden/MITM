from module.protocol.network.message import Message


class IconPresetSaveRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6308
        self.presetId = {"type": "int", "value": ""}
        self.symbolId = {"type": "uint", "value": ""}
        self.updateData = {"type": "Boolean", "value": ""}
