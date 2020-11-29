from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapObstacleUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5663
        self.vars.append({"name": "obstacles", "type": "Vector.<MapObstacle>", "value": ""})
