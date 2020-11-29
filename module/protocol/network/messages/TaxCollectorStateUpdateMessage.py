from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorStateUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5755
        self.vars.append({"name": "uniqueId", "type": "Number", "value": ""})
        self.vars.append({"name": "state", "type": "int", "value": ""})
