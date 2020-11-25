from module.protocol.network.message import Message


class PrismFightDefenderLeaveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9060
        self.subAreaId = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.fighterToRemoveId = {"type": "Number", "value": ""}
