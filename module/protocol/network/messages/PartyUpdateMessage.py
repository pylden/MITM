from module.protocol.network.message import Message


class PartyUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4697
        self.memberInformations = {"type": "PartyMemberInformations", "value": ""}
