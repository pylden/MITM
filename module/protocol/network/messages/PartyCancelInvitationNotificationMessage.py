from module.protocol.network.message import Message


class PartyCancelInvitationNotificationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1253
        self.cancelerId = {"type": "Number", "value": ""}
        self.guestId = {"type": "Number", "value": ""}
