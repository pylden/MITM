from module.protocol.network.message import Message


class PrismFightAttackerAddMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2846
        self.subAreaId = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.attacker = {"type": "CharacterMinimalPlusLookInformations", "value": ""}
