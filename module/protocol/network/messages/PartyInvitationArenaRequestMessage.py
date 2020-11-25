from module.protocol.network.message import Message


class PartyInvitationArenaRequestMessage(Message):
    def __init__(self):
        self.id = 8126
