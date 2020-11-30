from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StorageObjectUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1134
        self.object = {"type": "ObjectItem", "value": ""}
