from module.protocol.network.message import Message


class GameContextDestroyMessage(Message):
    def __init__(self):
        self.id = 5443
