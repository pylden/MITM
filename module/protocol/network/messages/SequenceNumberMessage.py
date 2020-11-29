from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SequenceNumberMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2848
        self.vars.append({"name": "number", "type": "uint", "value": ""})
