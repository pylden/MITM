from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendDeleteResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4241
        self.vars.append({"name": "success", "type": "Boolean", "value": ""})
        self.vars.append({"name": "name", "type": "String", "value": ""})
