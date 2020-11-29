from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AdminCommandMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5178
        self.vars.append({"name": "content", "type": "String", "value": ""})
