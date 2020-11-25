from module.protocol.network.message import Message


class PresetSaveErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8976
        self.presetId = {"type": "int", "value": ""}
        self.code = {"type": "uint", "value": ""}
