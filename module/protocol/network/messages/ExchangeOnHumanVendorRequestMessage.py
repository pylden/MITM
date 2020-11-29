from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeOnHumanVendorRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9270
        self.vars.append({"name": "humanVendorId", "type": "Number", "value": ""})
        self.vars.append({"name": "humanVendorCell", "type": "uint", "value": ""})
