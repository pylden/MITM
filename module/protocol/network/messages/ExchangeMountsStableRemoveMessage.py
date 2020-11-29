from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeMountsStableRemoveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9478
        self.vars.append({"name": "mountsId", "type": "Vector.<int>", "value": ""})
