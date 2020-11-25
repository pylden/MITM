from module.protocol.network.message import Message


class GameRolePlayAggressionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6136
        self.attackerId = {"type": "Number", "value": ""}
        self.defenderId = {"type": "Number", "value": ""}
