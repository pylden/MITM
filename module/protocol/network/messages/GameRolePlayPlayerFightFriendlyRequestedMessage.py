from module.protocol.network.message import Message


class GameRolePlayPlayerFightFriendlyRequestedMessage(Message):
    def __init__(self):
        self.id = 9866
