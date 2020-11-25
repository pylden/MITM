from module.protocol.network.message import Message


class GameRolePlayPlayerFightFriendlyAnsweredMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1392
        self.fightId = {"type": "uint", "value": ""}
        self.sourceId = {"type": "Number", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
