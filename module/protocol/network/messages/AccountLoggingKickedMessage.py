from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AccountLoggingKickedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1881
        self.vars.append({"name": "days", "type": "uint", "value": ""})
        self.vars.append({"name": "hours", "type": "uint", "value": ""})
        self.vars.append({"name": "minutes", "type": "uint", "value": ""})
