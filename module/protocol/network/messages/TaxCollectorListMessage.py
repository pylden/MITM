from module.protocol.network.message import Message


class TaxCollectorListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1980
        self.nbcollectorMax = {"type": "uint", "value": ""}
        self.fightersInformations = {"type": "Vector.<TaxCollectorFightersInformation>", "value": ""}
        self.infoType = {"type": "uint", "value": ""}
