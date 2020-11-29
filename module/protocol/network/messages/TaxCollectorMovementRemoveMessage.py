from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorMovementRemoveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6992
        self.vars.append({"name": "collectorId", "type": "Number", "value": ""})
