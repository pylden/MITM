from module.protocol.network.message import Message


class PartyInvitationCancelledForGuestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7061
        self.cancelerId = {"type": "Number", "value": ""}
