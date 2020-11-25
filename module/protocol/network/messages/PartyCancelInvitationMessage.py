from module.protocol.network.message import Message


class PartyCancelInvitationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7409
        self.guestId = {"type": "Number", "value": ""}
