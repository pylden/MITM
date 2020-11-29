from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AbstractTaxCollectorListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4914
        self.vars.append({"name": "informations", "type": "Vector.<TaxCollectorInformations>", "value": ""})
