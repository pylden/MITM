from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InventoryContentMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4140
        self.vars.append({"name": "objects", "type": "Vector.<ObjectItem>", "value": ""})
        self.vars.append({"name": "kamas", "type": "Number", "value": ""})
