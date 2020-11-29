from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicDateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4547
        self.vars.append({"name": "day", "type": "uint", "value": ""})
        self.vars.append({"name": "month", "type": "uint", "value": ""})
        self.vars.append({"name": "year", "type": "uint", "value": ""})
