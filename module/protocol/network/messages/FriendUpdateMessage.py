from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9116
        self.vars.append({"name": "friendUpdated", "type": "FriendInformations", "value": ""})
