from module.protocol.network.message import Message


class InvalidPresetsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2448
        self.presetIds = {"type": "Vector.<uint>", "value": ""}
