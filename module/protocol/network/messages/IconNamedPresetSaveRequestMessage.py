from module.protocol.network.message import Message


class IconNamedPresetSaveRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9336
        self.name = {"type": "String", "value": ""}
        self.type = {"type": "uint", "value": ""}
