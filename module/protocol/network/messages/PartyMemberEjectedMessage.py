from module.protocol.network.message import Message


class PartyMemberEjectedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7534
        self.kickerId = {"type": "Number", "value": ""}
