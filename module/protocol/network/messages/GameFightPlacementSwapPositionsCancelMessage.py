from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsCancelMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 533
        self.requestId = {"type": "uint", "value": ""}
