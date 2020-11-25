from module.protocol.network.message import Message


class PartyCancelInvitationNotificationMessage(Message):
    def __init__(self):
        self.id = 1253
