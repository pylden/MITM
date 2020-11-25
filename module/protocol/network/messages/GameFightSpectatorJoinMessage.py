from module.protocol.network.message import Message


class GameFightSpectatorJoinMessage(Message):
    def __init__(self):
        self.id = 6917
