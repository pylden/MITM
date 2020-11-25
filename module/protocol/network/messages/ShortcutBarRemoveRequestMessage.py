from module.protocol.network.message import Message


class ShortcutBarRemoveRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 373
        self.barType = {"type": "uint", "value": ""}
        self.slot = {"type": "uint", "value": ""}
