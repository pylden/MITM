from module.protocol.network.message import Message


class GameFightJoinMessage(Message):
    def __init__(self):
        self.id = 2650
