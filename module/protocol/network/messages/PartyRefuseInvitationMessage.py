from module.protocol.network.message import Message


class PartyRefuseInvitationMessage(Message):
    def __init__(self):
        self.id = 1909
