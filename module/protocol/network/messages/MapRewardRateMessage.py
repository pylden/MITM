from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapRewardRateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9715
        self.mapRate = {"type": "int", "value": ""}
        self.subAreaRate = {"type": "int", "value": ""}
        self.totalRate = {"type": "int", "value": ""}
