from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeMultiCraftCrafterCanUseHisRessourcesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5515
        self.allowed = {"type": "Boolean", "value": ""}
