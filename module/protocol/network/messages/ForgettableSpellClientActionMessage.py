from module.protocol.network.message import Message


class ForgettableSpellClientActionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6056
        self.spellId = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
