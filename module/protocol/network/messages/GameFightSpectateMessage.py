from module.protocol.network.message import Message


class GameFightSpectateMessage(Message):
    def __init__(self):
        self.id = 6511
