from module.protocol.network.message import Message


class GameEntityDispositionErrorMessage(Message):
    def __init__(self):
        self.id = 6347
