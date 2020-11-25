from module.protocol.network.message import Message


class GameRolePlayAggressionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6136
        self.attackerId = {"type": "Number", "value": ""}
        self.defenderId = {"type": "Number", "value": ""}
