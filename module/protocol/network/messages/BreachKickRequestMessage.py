from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachKickRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8280
        self.vars.append({"name": "target", "type": "Number", "value": ""})
