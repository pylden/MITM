from module.protocol.network.message import Message


class GameFightNewRoundMessage(Message):
    def __init__(self):
        self.id = 9076
