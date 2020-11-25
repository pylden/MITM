from module.protocol.network.message import Message


class TaxCollectorListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1980
        self.nbcollectorMax = {"type": "uint", "value": ""}
        self.fightersInformations = {"type": "Vector.<TaxCollectorFightersInformation>", "value": ""}
        self.infoType = {"type": "uint", "value": ""}
