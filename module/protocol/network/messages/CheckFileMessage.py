from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CheckFileMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8145
        self.vars.append({"name": "filenameHash", "type": "String", "value": ""})
        self.vars.append({"name": "type", "type": "uint", "value": ""})
        self.vars.append({"name": "value", "type": "String", "value": ""})
