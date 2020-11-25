from module.protocol.network.message import Message


class ForgettableSpellDeleteMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8765
        self.reason = {"type": "uint", "value": ""}
        self.spells = {"type": "Vector.<uint>", "value": ""}
