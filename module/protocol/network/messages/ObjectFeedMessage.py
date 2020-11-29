from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectFeedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5627
        self.vars.append({"name": "objectUID", "type": "uint", "value": ""})
        self.vars.append({"name": "meal", "type": "Vector.<ObjectItemQuantity>", "value": ""})
