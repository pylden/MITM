from module.protocol.network.message import Message


class GameRolePlayPlayerFightFriendlyAnsweredMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1392
        self.fightId = {"type": "uint", "value": ""}
        self.sourceId = {"type": "Number", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
