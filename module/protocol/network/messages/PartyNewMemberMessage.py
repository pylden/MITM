from module.protocol.network.message import Message


class PartyNewMemberMessage(Message):
    def __init__(self):
        self.id = 2531
