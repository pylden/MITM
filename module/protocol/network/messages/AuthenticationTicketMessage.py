from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AuthenticationTicketMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8374
        self.vars.append({"name": "lang", "type": "String", "value": ""})
        self.vars.append({"name": "ticket", "type": "String", "value": ""})
