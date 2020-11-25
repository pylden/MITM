from module.protocol.network.message import Message


class GameFightSpectatePlayerRequestMessage(Message):
    def __init__(self):
        self.id = 4807
