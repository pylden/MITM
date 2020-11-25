from module.protocol.network.message import Message


class PresetDeleteResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9792
        self.presetId = {"type": "int", "value": ""}
        self.code = {"type": "uint", "value": ""}
