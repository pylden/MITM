from module.protocol.network.message import Message


class ChatCommunityChannelCommunityMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7105
        self.communityId = {"type": "int", "value": ""}
