from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4410
        self.object = {"type": "ObjectItem", "value": ""}
        self.origin = {"type": "uint", "value": ""}
