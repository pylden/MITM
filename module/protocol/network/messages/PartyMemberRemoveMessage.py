from module.protocol.network.message import Message


class PartyMemberRemoveMessage(Message):
    def __init__(self):
        self.id = 2903
