from module.protocol.network.message import Message


class GameMapNoMovementMessage(Message):
    def __init__(self):
        self.id = 6980
