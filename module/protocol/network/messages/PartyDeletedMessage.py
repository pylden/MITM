from module.protocol.network.message import Message


class PartyDeletedMessage(Message):
    def __init__(self):
        self.id = 2538
