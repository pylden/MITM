from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GoldAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1942
        self.vars.append({"name": "gold", "type": "GoldItem", "value": ""})
