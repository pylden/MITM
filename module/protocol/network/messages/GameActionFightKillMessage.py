from module.protocol.network.message import Message


class GameActionFightKillMessage(Message):
    def __init__(self):
        self.id = 8096
