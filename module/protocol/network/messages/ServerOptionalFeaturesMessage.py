from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ServerOptionalFeaturesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2305
        self.vars.append({"name": "features", "type": "Vector.<uint>", "value": ""})
