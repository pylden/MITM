from module.protocol.network.message import Message


class GameRolePlayArenaUnregisterMessage(Message):
    def __init__(self):
        self.id = 7305
