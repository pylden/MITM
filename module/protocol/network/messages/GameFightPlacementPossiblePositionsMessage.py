from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementPossiblePositionsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8748
        self.positionsForChallengers = {"type": "Vector.<uint>", "value": ""}
        self.positionsForDefenders = {"type": "Vector.<uint>", "value": ""}
        self.teamNumber = {"type": "uint", "value": ""}
