from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ServerSessionConstantsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9947
        self.variables = {"type": "Vector.<ServerSessionConstant>", "value": ""}
