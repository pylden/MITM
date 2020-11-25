from module.protocol.network.message import Message


class GameRolePlayPlayerFightFriendlyAnswerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2509
        self.fightId = {"type": "uint", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
