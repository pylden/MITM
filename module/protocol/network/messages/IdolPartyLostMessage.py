from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdolPartyLostMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2578
        self.vars.append({"name": "idolId", "type": "uint", "value": ""})
