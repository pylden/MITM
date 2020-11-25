from module.protocol.network.message import Message


class GameFightTurnListMessage(Message):
    def __init__(self):
        self.id = 399
