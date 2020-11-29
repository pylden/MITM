from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachSavedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8940
        self.vars.append({"name": "saved", "type": "Boolean", "value": ""})
