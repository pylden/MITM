from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsCancelledMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 898
        self.requestId = {"type": "uint", "value": ""}
        self.cancellerId = {"type": "Number", "value": ""}
