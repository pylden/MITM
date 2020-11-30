from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsOfferMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 568
        self.requestId = {"type": "uint", "value": ""}
        self.requesterId = {"type": "Number", "value": ""}
        self.requesterCellId = {"type": "uint", "value": ""}
        self.requestedId = {"type": "Number", "value": ""}
        self.requestedCellId = {"type": "uint", "value": ""}
