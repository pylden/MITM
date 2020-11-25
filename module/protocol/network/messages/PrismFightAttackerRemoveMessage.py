from module.protocol.network.message import Message


class PrismFightAttackerRemoveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6001
        self.subAreaId = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.fighterToRemoveId = {"type": "Number", "value": ""}
