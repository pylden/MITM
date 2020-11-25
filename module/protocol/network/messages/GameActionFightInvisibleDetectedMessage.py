from module.protocol.network.message import Message


class GameActionFightInvisibleDetectedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2560
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "int", "value": ""}
