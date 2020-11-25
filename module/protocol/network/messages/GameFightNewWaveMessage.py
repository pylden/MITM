from module.protocol.network.message import Message


class GameFightNewWaveMessage(Message):
    def __init__(self):
        self.id = 5791
