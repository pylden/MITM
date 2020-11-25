from module.protocol.network.message import Message


class GameFightSynchronizeMessage(Message):
    def __init__(self):
        self.id = 276
