from module.protocol.network.message import Message


class GameActionFightSlideMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9185
        self.targetId = {"type": "Number", "value": ""}
        self.startCellId = {"type": "int", "value": ""}
        self.endCellId = {"type": "int", "value": ""}
