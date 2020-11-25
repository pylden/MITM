from module.protocol.network.message import Message


class GameActionFightCarryCharacterMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5624
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "int", "value": ""}
