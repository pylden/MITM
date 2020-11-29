from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseInListAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9210
        self.vars.append({"name": "itemUID", "type": "int", "value": ""})
        self.vars.append({"name": "objectGID", "type": "uint", "value": ""})
        self.vars.append({"name": "objectType", "type": "uint", "value": ""})
        self.vars.append({"name": "effects", "type": "Vector.<ObjectEffect>", "value": ""})
        self.vars.append({"name": "prices", "type": "Vector.<Number>", "value": ""})
