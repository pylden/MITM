from module.protocol.network.message import Message


class GameActionFightDeathMessage(Message):
    def __init__(self):
        self.id = 4815
