from module.protocol.network.message import Message


class PartyInvitationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4087
        self.partyName = {"type": "String", "value": ""}
        self.fromName = {"type": "String", "value": ""}
