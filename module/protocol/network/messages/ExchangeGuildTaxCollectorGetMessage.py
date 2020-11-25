from module.protocol.network.message import Message


class ExchangeGuildTaxCollectorGetMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
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
