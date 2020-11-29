from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendAddRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5946
        self.vars.append({"name": "name", "type": "String", "value": ""})
