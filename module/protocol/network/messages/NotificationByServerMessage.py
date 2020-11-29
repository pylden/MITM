from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NotificationByServerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 312
        self.vars.append({"name": "id", "type": "uint", "value": ""})
        self.vars.append({"name": "parameters", "type": "Vector.<String>", "value": ""})
        self.vars.append({"name": "forceOpen", "type": "Boolean", "value": ""})
