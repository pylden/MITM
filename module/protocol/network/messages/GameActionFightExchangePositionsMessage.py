from module.protocol.network.message import Message


class GameActionFightExchangePositionsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 753
        self.targetId = {"type": "Number", "value": ""}
        self.casterCellId = {"type": "int", "value": ""}
        self.targetCellId = {"type": "int", "value": ""}
