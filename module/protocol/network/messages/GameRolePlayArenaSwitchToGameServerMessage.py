from module.protocol.network.message import Message


class GameRolePlayArenaSwitchToGameServerMessage(Message):
    def __init__(self):
        self.id = 6269
