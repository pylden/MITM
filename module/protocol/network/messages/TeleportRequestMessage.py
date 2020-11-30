from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1080
        self.sourceType = {"type": "uint", "value": ""}
        self.destinationType = {"type": "uint", "value": ""}
        self.mapId = {"type": "Number", "value": ""}
