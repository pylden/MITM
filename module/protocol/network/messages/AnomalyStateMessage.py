from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AnomalyStateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4556
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "open", "type": "Boolean", "value": ""})
        self.vars.append({"name": "closingTime", "type": "Number", "value": ""})
