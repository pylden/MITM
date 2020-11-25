from module.protocol.network.message import Message


class PartyInvitationDetailsRequestMessage(Message):
    def __init__(self):
        self.id = 182
