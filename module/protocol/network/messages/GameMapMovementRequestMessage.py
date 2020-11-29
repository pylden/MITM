from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameMapMovementRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7064
        self.vars.append({"name": "keyMovements", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
