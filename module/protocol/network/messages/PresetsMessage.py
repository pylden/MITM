from module.protocol.network.message import Message


class PresetsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1558
        self.presets = {"type": "Vector.<Preset>", "value": ""}
