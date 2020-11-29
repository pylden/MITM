from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4410
        self.vars.append({"name": "object", "type": "ObjectItem", "value": ""})
        self.vars.append({"name": "origin", "type": "uint", "value": ""})
