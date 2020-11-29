from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HavenBagPackListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6073
        self.vars.append({"name": "packIds", "type": "Vector.<int>", "value": ""})
