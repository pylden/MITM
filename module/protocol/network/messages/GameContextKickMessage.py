from module.protocol.network.message import Message


class GameContextKickMessage(Message):
    def __init__(self):
        self.id = 7244