from module.protocol.network.messages.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage


class TaxCollectorListMessage(AbstractTaxCollectorListMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractTaxCollectorListMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1980
        self.vars.append({"name": "nbcollectorMax", "type": "uint", "value": ""})
        self.vars.append({"name": "fightersInformations", "type": "Vector.<TaxCollectorFightersInformation>", "value": ""})
        self.vars.append({"name": "infoType", "type": "uint", "value": ""})
