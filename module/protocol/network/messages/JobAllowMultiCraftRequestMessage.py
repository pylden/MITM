from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobAllowMultiCraftRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3569
        self.vars.append({"name": "enabled", "type": "Boolean", "value": ""})
