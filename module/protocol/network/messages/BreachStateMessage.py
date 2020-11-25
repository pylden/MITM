from module.protocol.network.message import Message


class BreachStateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4331
        self.owner = {"type": "CharacterMinimalInformations", "value": ""}
        self.bonuses = {"type": "Vector.<ObjectEffectInteger>", "value": ""}
        self.bugdet = {"type": "uint", "value": ""}
        self.saved = {"type": "Boolean", "value": ""}
