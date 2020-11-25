from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsOfferMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 568
        self.requestId = {"type": "uint", "value": ""}
        self.requesterId = {"type": "Number", "value": ""}
        self.requesterCellId = {"type": "uint", "value": ""}
        self.requestedId = {"type": "Number", "value": ""}
        self.requestedCellId = {"type": "uint", "value": ""}
