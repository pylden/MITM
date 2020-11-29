from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ClientUIOpenedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1056
        self.vars.append({"name": "type", "type": "uint", "value": ""})
