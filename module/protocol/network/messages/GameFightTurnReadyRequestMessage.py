from module.protocol.network.message import Message


class GameFightTurnReadyRequestMessage(Message):
    def __init__(self):
        self.id = 9704
