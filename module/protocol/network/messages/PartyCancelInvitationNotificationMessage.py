from module.protocol.network.message import Message


class PartyCancelInvitationNotificationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1253
        self.cancelerId = {"type": "Number", "value": ""}
        self.guestId = {"type": "Number", "value": ""}
