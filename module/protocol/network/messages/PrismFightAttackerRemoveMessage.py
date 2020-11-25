from module.protocol.network.message import Message


class PrismFightAttackerRemoveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6001
        self.subAreaId = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.fighterToRemoveId = {"type": "Number", "value": ""}
