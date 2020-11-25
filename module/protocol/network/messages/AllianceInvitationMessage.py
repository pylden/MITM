from module.protocol.network.message import Message


class AllianceInvitationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7156
        self.targetId = {"type": "Number", "value": ""}
