from module.protocol.network.message import Message


class GameContextCreateErrorMessage(Message):
    def __init__(self):
        self.id = 2151
