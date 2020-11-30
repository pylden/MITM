from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeGuildTaxCollectorGetMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2767
        self.collectorName = {"type": "String", "value": ""}
        self.worldX = {"type": "int", "value": ""}
        self.worldY = {"type": "int", "value": ""}
        self.mapId = {"type": "Number", "value": ""}
        self.subAreaId = {"type": "uint", "value": ""}
        self.userName = {"type": "String", "value": ""}
        self.callerId = {"type": "Number", "value": ""}
        self.callerName = {"type": "String", "value": ""}
        self.experience = {"type": "Number", "value": ""}
        self.pods = {"type": "uint", "value": ""}
        self.objectsInfos = {"type": "Vector.<ObjectItemGenericQuantity>", "value": ""}
