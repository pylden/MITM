from module.protocol.network.message import Message


class PartyInvitationRequestMessage(Message):
    def __init__(self):
        self.id = 1758
        self.name = {"type": "String", "value": ""}
