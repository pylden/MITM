from module.protocol.network.message import Message


class PartyMemberEjectedMessage(Message):
    def __init__(self):
        self.id = 7534