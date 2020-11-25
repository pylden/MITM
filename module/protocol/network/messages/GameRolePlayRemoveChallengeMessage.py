from module.protocol.network.message import Message


class GameRolePlayRemoveChallengeMessage(Message):
    def __init__(self):
        self.id = 889
