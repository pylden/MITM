from module.protocol.network.message import Message


class ForgettableSpellDeleteMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8765
        self.reason = {"type": "uint", "value": ""}
        self.spells = {"type": "Vector.<uint>", "value": ""}
