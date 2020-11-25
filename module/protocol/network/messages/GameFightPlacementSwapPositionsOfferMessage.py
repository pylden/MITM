from module.protocol.network.message import Message


class GameFightPlacementSwapPositionsOfferMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 568
        self.requestId = {"type": "uint", "value": ""}
        self.requesterId = {"type": "Number", "value": ""}
        self.requesterCellId = {"type": "uint", "value": ""}
        self.requestedId = {"type": "Number", "value": ""}
        self.requestedCellId = {"type": "uint", "value": ""}
