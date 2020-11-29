from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChatErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5057
        self.vars.append({"name": "reason", "type": "uint", "value": ""})
