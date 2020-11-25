from module.protocol.network.message import Message


class AllianceInvitationStateRecrutedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5125
        self.invitationState = {"type": "uint", "value": ""}
