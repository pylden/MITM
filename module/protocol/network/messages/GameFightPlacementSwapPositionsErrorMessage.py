from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsErrorMessage(Message):
    def __init__(self):
        self.id = 9407
