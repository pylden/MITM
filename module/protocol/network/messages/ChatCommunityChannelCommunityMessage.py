from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChatCommunityChannelCommunityMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7105
        self.vars.append({"name": "communityId", "type": "int", "value": ""})
