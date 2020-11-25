from module.protocol.network.message import Message


class SocialNoticeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1521
        self.content = {"type": "String", "value": ""}
        self.timestamp = {"type": "uint", "value": ""}
        self.memberId = {"type": "Number", "value": ""}
        self.memberName = {"type": "String", "value": ""}
