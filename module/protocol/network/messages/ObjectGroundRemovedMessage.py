from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectGroundRemovedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1247
        self.cell = {"type": "uint", "value": ""}
