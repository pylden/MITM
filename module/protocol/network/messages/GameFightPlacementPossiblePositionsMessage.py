from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementPossiblePositionsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8748
        self.vars.append({"name": "positionsForChallengers", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "positionsForDefenders", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "teamNumber", "type": "uint", "value": ""})
