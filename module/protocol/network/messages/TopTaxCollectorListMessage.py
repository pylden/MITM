from module.protocol.network.messages.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage


class TopTaxCollectorListMessage(AbstractTaxCollectorListMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractTaxCollectorListMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3788
        self.vars.append({"name": "isDungeon", "type": "Boolean", "value": ""})
