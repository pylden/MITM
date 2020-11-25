from module.protocol.network.message import Message


class GameRolePlayRemoveChallengeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 889
        self.fightId = {"type": "uint", "value": ""}
