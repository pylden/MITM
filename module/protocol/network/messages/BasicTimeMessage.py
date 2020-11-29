from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicTimeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1002
        self.vars.append({"name": "timestamp", "type": "Number", "value": ""})
        self.vars.append({"name": "timezoneOffset", "type": "int", "value": ""})
