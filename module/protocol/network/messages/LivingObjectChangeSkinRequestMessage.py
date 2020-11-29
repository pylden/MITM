from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LivingObjectChangeSkinRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1423
        self.vars.append({"name": "livingUID", "type": "uint", "value": ""})
        self.vars.append({"name": "livingPosition", "type": "uint", "value": ""})
        self.vars.append({"name": "skinId", "type": "uint", "value": ""})
