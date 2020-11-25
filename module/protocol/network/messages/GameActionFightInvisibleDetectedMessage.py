from module.protocol.network.message import Message


class GameActionFightInvisibleDetectedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2560
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "int", "value": ""}
