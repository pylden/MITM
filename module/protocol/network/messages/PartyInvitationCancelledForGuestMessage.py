from module.protocol.network.message import Message


class PartyInvitationCancelledForGuestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7061
        self.cancelerId = {"type": "Number", "value": ""}
