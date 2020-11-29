from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DecraftResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8523
        self.vars.append({"name": "results", "type": "Vector.<DecraftedItemStackInfo>", "value": ""})
