from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MailStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3369
        self.vars.append({"name": "unread", "type": "uint", "value": ""})
        self.vars.append({"name": "total", "type": "uint", "value": ""})
