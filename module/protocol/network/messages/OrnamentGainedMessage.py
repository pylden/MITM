from module.protocol.network.messages.NetworkMessage import NetworkMessage


class OrnamentGainedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3842
        self.vars.append({"name": "ornamentId", "type": "uint", "value": ""})
