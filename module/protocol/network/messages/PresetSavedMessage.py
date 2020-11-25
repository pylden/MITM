from module.protocol.network.message import Message


class PresetSavedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4545
        self.presetId = {"type": "int", "value": ""}
        self.preset = {"type": "Preset", "value": ""}
