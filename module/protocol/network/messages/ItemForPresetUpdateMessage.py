from module.protocol.network.message import Message


class ItemForPresetUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8924
        self.presetId = {"type": "int", "value": ""}
        self.presetItem = {"type": "ItemForPreset", "value": ""}
