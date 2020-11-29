from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StorageObjectsRemoveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5584
        self.vars.append({"name": "objectUIDList", "type": "Vector.<uint>", "value": ""})
