from module.protocol.network.message import Message


class ChatCommunityChannelSetCommunityRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2713
        self.communityId = {"type": "int", "value": ""}
