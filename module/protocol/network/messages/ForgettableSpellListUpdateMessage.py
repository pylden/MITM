from module.protocol.network.message import Message


class ForgettableSpellListUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1059
        self.action = {"type": "uint", "value": ""}
        self.spells = {"type": "Vector.<ForgettableSpellItem>", "value": ""}
