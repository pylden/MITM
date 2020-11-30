from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StorageObjectRemoveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6168
        self.objectUID = {"type": "uint", "value": ""}
