from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockBuyRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6999
        self.vars.append({"name": "proposedPrice", "type": "Number", "value": ""})
