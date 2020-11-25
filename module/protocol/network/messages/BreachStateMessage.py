from module.protocol.network.message import Message


class BreachStateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4331
        self.owner = {"type": "CharacterMinimalInformations", "value": ""}
        self.bonuses = {"type": "Vector.<ObjectEffectInteger>", "value": ""}
        self.bugdet = {"type": "uint", "value": ""}
        self.saved = {"type": "Boolean", "value": ""}
