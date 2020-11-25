from module.protocol.network.message import Message


class SocialNoticeMessage(Message):
    def __init__(self):
        self.id = 1521
        self.content = {"type": "String", "value": ""}
        self.memberName = {"type": "String", "value": ""}
