from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameMapMovementCancelMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 615
        self.vars.append({"name": "cellId", "type": "uint", "value": ""})
