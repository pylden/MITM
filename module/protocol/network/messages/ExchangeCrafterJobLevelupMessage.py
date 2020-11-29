from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeCrafterJobLevelupMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8633
        self.vars.append({"name": "crafterJobLevel", "type": "uint", "value": ""})
