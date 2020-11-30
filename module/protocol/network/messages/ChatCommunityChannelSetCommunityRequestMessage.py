from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChatCommunityChannelSetCommunityRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2713
        self.communityId = {"type": "int", "value": ""}
