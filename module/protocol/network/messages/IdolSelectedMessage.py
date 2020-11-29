from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdolSelectedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 704
        self.vars.append({"name": "idolId", "type": "uint", "value": ""})
        self.vars.append({"name": "activate", "type": "Boolean", "value": ""})
        self.vars.append({"name": "party", "type": "Boolean", "value": ""})
