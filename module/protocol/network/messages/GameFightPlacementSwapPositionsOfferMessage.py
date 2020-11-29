from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsOfferMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 568
        self.vars.append({"name": "requestId", "type": "uint", "value": ""})
        self.vars.append({"name": "requesterId", "type": "Number", "value": ""})
        self.vars.append({"name": "requesterCellId", "type": "uint", "value": ""})
        self.vars.append({"name": "requestedId", "type": "Number", "value": ""})
        self.vars.append({"name": "requestedCellId", "type": "uint", "value": ""})
