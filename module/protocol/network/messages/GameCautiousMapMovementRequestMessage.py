from module.protocol.network.message import Message


class GameCautiousMapMovementRequestMessage(Message):
    def __init__(self):
        self.id = 189
