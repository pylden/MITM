from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeGuildTaxCollectorGetMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2767
        self.vars.append({"name": "collectorName", "type": "String", "value": ""})
        self.vars.append({"name": "worldX", "type": "int", "value": ""})
        self.vars.append({"name": "worldY", "type": "int", "value": ""})
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "userName", "type": "String", "value": ""})
        self.vars.append({"name": "callerId", "type": "Number", "value": ""})
        self.vars.append({"name": "callerName", "type": "String", "value": ""})
        self.vars.append({"name": "experience", "type": "Number", "value": ""})
        self.vars.append({"name": "pods", "type": "uint", "value": ""})
        self.vars.append({"name": "objectsInfos", "type": "Vector.<ObjectItemGenericQuantity>", "value": ""})
