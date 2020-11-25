from module.protocol.network.message import Message


class PresetUseRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3898
        self.presetId = {"type": "int", "value": ""}
