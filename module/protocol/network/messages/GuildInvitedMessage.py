from module.protocol.network.message import Message


class GuildInvitedMessage(Message):
    def __init__(self):
        self.id = 3856
        self.recruterName = {"type": "String", "value": ""}
