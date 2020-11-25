from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsCancelMessage(Message):
    def __init__(self):
        self.id = 533
