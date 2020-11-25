from module.protocol.network.message import Message


class PartyLocateMembersRequestMessage(Message):
    def __init__(self):
        self.id = 3120
