from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LivingObjectMessageMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9436
        self.vars.append({"name": "msgId", "type": "uint", "value": ""})
        self.vars.append({"name": "timeStamp", "type": "uint", "value": ""})
        self.vars.append({"name": "owner", "type": "String", "value": ""})
        self.vars.append({"name": "objectGenericId", "type": "uint", "value": ""})
