from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsMessage(Message):
    def __init__(self):
        self.id = 4901
