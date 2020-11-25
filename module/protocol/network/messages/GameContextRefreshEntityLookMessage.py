from module.protocol.network.message import Message


class GameContextRefreshEntityLookMessage(Message):
    def __init__(self):
        self.id = 5695
