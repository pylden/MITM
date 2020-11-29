from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiConfirmationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3477
        self.vars.append({"name": "kamas", "type": "Number", "value": ""})
        self.vars.append({"name": "ogrines", "type": "Number", "value": ""})
        self.vars.append({"name": "rate", "type": "uint", "value": ""})
        self.vars.append({"name": "action", "type": "uint", "value": ""})
