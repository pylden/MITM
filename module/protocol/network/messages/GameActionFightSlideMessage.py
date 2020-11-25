from module.protocol.network.message import Message


class GameActionFightSlideMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9185
        self.targetId = {"type": "Number", "value": ""}
        self.startCellId = {"type": "int", "value": ""}
        self.endCellId = {"type": "int", "value": ""}
