from module.protocol.network.message import Message


class GameRolePlayShowChallengeMessage(Message):
    def __init__(self):
        self.id = 5095
