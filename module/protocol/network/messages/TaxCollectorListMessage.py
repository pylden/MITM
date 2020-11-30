from module.protocol.network.messages.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage


class TaxCollectorListMessage(AbstractTaxCollectorListMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractTaxCollectorListMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1980
        self.nbcollectorMax = {"type": "uint", "value": ""}
        self.fightersInformations = {"type": "Vector.<TaxCollectorFightersInformation>", "value": ""}
        self.infoType = {"type": "uint", "value": ""}
