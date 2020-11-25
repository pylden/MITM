from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsAcceptMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5750
        self.requestId = {"type": "uint", "value": ""}
