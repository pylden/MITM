from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsCancelledMessage(Message):
    def __init__(self):
        self.id = 898
