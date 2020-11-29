from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeSetCraftRecipeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 49
        self.vars.append({"name": "objectGID", "type": "uint", "value": ""})
