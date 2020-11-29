from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorMovementAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9684
        self.vars.append({"name": "informations", "type": "TaxCollectorInformations", "value": ""})
