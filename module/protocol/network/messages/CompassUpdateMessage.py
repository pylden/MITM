from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CompassUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3439
        self.type = {"type": "uint", "value": ""}
        self.coords = {"type": "MapCoordinates", "value": ""}
