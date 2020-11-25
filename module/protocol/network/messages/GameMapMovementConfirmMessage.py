from module.protocol.network.message import Message


class GameMapMovementConfirmMessage(Message):
    def __init__(self):
        self.id = 7525
