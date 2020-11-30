from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightLeaveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8271
        self.charId = {"type": "Number", "value": ""}
