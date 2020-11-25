from module.protocol.network.message import Message


class PartyLocateMembersMessage(Message):
    def __init__(self):
        self.id = 2685
