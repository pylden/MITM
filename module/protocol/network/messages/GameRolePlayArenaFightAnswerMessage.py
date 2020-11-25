from module.protocol.network.message import Message


class GameRolePlayArenaFightAnswerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2334
        self.fightId = {"type": "uint", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
