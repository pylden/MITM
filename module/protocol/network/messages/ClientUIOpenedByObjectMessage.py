from module.protocol.network.messages.ClientUIOpenedMessage import ClientUIOpenedMessage


class ClientUIOpenedByObjectMessage(ClientUIOpenedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ClientUIOpenedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2095
        self.vars.append({"name": "uid", "type": "uint", "value": ""})
