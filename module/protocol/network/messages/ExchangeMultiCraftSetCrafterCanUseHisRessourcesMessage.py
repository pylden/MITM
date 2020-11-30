from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2395
        self.allow = {"type": "Boolean", "value": ""}
