from module.protocol.network.message import Message


class GameRolePlayRemoveChallengeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 889
        self.fightId = {"type": "uint", "value": ""}
