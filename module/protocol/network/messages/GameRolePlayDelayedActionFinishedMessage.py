from module.protocol.network.message import Message


class GameRolePlayDelayedActionFinishedMessage(Message):
    def __init__(self):
        self.id = 1897
