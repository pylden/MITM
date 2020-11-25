from module.protocol.network.message import Message


class GameFightTurnReadyMessage(Message):
    def __init__(self):
        self.id = 983
