from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 399
        self.ids = {"type": "Vector.<Number>", "value": ""}
        self.deadsIds = {"type": "Vector.<Number>", "value": ""}
