from module.protocol.network.message import Message


class PrismFightDefenderAddMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1666
        self.subAreaId = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.defender = {"type": "CharacterMinimalPlusLookInformations", "value": ""}
