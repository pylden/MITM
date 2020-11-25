from module.protocol.network.message import Message


class GameActionFightExchangePositionsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 753
        self.targetId = {"type": "Number", "value": ""}
        self.casterCellId = {"type": "int", "value": ""}
        self.targetCellId = {"type": "int", "value": ""}
