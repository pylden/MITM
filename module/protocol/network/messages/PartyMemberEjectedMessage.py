from module.protocol.network.message import Message


class PartyMemberEjectedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7534
        self.kickerId = {"type": "Number", "value": ""}
