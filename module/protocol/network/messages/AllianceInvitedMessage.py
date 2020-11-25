from module.protocol.network.message import Message


class AllianceInvitedMessage(Message):
    def __init__(self):
        self.id = 6002
        self.recruterName = {"type": "String", "value": ""}
