from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StorageObjectsUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5590
        self.objectList = {"type": "Vector.<ObjectItem>", "value": ""}
