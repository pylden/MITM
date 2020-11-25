from module.protocol.network.message import Message


class GameActionFightTriggerGlyphTrapMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9588
        self.markId = {"type": "int", "value": ""}
        self.markImpactCell = {"type": "uint", "value": ""}
        self.triggeringCharacterId = {"type": "Number", "value": ""}
        self.triggeredSpellId = {"type": "uint", "value": ""}
