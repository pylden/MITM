from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LivingObjectMessageRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4103
        self.vars.append({"name": "msgId", "type": "uint", "value": ""})
        self.vars.append({"name": "parameters", "type": "Vector.<String>", "value": ""})
        self.vars.append({"name": "livingObject", "type": "uint", "value": ""})
