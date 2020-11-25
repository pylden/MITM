from module.protocol.network.message import Message


class GameFightPlacementPossiblePositionsMessage(Message):
    def __init__(self):
        self.id = 8748
