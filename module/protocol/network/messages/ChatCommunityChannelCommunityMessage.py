from module.protocol.network.message import Message


class ChatCommunityChannelCommunityMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7105
        self.communityId = {"type": "int", "value": ""}
