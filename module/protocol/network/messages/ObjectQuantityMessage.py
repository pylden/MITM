from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectQuantityMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9459
        self.vars.append({"name": "objectUID", "type": "uint", "value": ""})
        self.vars.append({"name": "quantity", "type": "uint", "value": ""})
        self.vars.append({"name": "origin", "type": "uint", "value": ""})
