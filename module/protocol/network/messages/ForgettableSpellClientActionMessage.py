from module.protocol.network.message import Message


class ForgettableSpellClientActionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6056
        self.spellId = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
