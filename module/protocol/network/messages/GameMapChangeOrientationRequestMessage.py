from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameMapChangeOrientationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1337
        self.vars.append({"name": "direction", "type": "uint", "value": ""})
