from module.protocol.network.message import Message


class PartyInvitationCancelledForGuestMessage(Message):
    def __init__(self):
        self.id = 7061
