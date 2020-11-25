from module.protocol.network.message import Message


class PartyKickRequestMessage(Message):
    def __init__(self):
        self.id = 4770
