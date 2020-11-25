from module.protocol.network.message import Message


class PartyInvitationDetailsMessage(Message):
    def __init__(self):
        self.id = 7323
        self.partyName = {"type": "String", "value": ""}
        self.fromName = {"type": "String", "value": ""}
