from module.protocol.network.message import Message


class GameFightTurnFinishMessage(Message):
    def __init__(self):
        self.id = 385
