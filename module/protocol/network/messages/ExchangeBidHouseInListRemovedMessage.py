from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseInListRemovedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6283
        self.vars.append({"name": "itemUID", "type": "int", "value": ""})
        self.vars.append({"name": "objectGID", "type": "uint", "value": ""})
        self.vars.append({"name": "objectType", "type": "uint", "value": ""})
