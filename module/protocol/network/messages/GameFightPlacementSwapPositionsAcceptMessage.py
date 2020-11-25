from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsAcceptMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5750
        self.requestId = {"type": "uint", "value": ""}
