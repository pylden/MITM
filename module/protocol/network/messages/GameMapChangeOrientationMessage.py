from module.protocol.network.message import Message


class GameMapChangeOrientationMessage(Message):
    def __init__(self):
        self.id = 8450
