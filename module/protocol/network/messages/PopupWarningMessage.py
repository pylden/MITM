from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PopupWarningMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6411
        self.vars.append({"name": "lockDuration", "type": "uint", "value": ""})
        self.vars.append({"name": "author", "type": "String", "value": ""})
        self.vars.append({"name": "content", "type": "String", "value": ""})
