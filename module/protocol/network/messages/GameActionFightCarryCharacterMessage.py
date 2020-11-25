from module.protocol.network.message import Message


class GameActionFightCarryCharacterMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5624
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "int", "value": ""}
