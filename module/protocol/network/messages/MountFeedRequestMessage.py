from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountFeedRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1812
        self.vars.append({"name": "mountUid", "type": "uint", "value": ""})
        self.vars.append({"name": "mountLocation", "type": "int", "value": ""})
        self.vars.append({"name": "mountFoodUid", "type": "uint", "value": ""})
        self.vars.append({"name": "quantity", "type": "uint", "value": ""})
