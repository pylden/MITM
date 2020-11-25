from module.protocol.network.message import Message


class GameContextMoveElementMessage(Message):
    def __init__(self):
        self.id = 8769
