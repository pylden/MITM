from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsAcceptMessage(Message):
    def __init__(self):
        self.id = 5750
