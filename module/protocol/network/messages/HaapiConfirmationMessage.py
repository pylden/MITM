from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiConfirmationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7797
        self.vars.append({"name": "kamas", "type": "Number", "value": ""})
        self.vars.append({"name": "amount", "type": "Number", "value": ""})
        self.vars.append({"name": "rate", "type": "uint", "value": ""})
        self.vars.append({"name": "action", "type": "uint", "value": ""})
        self.vars.append({"name": "transaction", "type": "String", "value": ""})
