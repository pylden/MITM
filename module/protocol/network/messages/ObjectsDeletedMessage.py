from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectsDeletedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5628
        self.objectUID = {"type": "Vector.<uint>", "value": ""}
