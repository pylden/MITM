from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectSetPositionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1317
        self.vars.append({"name": "objectUID", "type": "uint", "value": ""})
        self.vars.append({"name": "position", "type": "uint", "value": ""})
        self.vars.append({"name": "quantity", "type": "uint", "value": ""})
