from module.protocol.network.message import Message


class PresetSaveErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8976
        self.presetId = {"type": "int", "value": ""}
        self.code = {"type": "uint", "value": ""}
