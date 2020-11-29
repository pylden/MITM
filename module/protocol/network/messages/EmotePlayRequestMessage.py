from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EmotePlayRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9094
        self.vars.append({"name": "emoteId", "type": "uint", "value": ""})
