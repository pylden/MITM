from module.protocol.network.message import Message


class GameEntityDispositionMessage(Message):
    def __init__(self):
        self.id = 3301
