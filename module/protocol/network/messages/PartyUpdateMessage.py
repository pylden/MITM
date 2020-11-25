from module.protocol.network.message import Message


class PartyUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4697
        self.memberInformations = {"type": "PartyMemberInformations", "value": ""}
