from module.protocol.network.message import Message


class PartyAcceptInvitationMessage(Message):
    def __init__(self):
        self.id = 8622
