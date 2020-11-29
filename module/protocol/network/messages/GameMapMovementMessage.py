from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameMapMovementMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8712
        self.vars.append({"name": "keyMovements", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "forcedDirection", "type": "int", "value": ""})
        self.vars.append({"name": "actorId", "type": "Number", "value": ""})
