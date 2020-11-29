from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChatAbstractServerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1532
        self.vars.append({"name": "channel", "type": "uint", "value": ""})
        self.vars.append({"name": "content", "type": "String", "value": ""})
        self.vars.append({"name": "timestamp", "type": "uint", "value": ""})
        self.vars.append({"name": "fingerprint", "type": "String", "value": ""})
