from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismsListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3577
        self.vars.append({"name": "prisms", "type": "Vector.<PrismSubareaEmptyInfo>", "value": ""})
