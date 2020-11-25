from module.protocol.network.message import Message


class PartyLeaveRequestMessage(Message):
    def __init__(self):
        self.id = 6383
