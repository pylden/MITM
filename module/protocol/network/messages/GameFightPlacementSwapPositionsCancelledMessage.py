from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsCancelledMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 898
        self.requestId = {"type": "uint", "value": ""}
        self.cancellerId = {"type": "Number", "value": ""}
