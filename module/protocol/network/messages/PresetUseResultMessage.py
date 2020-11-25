from module.protocol.network.message import Message


class PresetUseResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3758
        self.presetId = {"type": "int", "value": ""}
        self.code = {"type": "uint", "value": ""}
