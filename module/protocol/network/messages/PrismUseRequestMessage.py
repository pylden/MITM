from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismUseRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6760
        self.vars.append({"name": "moduleToUse", "type": "uint", "value": ""})
