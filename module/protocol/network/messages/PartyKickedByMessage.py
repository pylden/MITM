from module.protocol.network.message import Message


class PartyKickedByMessage(Message):
    def __init__(self):
        self.id = 2914
