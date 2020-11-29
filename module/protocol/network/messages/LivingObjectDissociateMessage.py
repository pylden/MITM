from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LivingObjectDissociateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6028
        self.vars.append({"name": "livingUID", "type": "uint", "value": ""})
        self.vars.append({"name": "livingPosition", "type": "uint", "value": ""})
