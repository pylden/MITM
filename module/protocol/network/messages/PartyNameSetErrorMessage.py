from module.protocol.network.message import Message


class PartyNameSetErrorMessage(Message):
    def __init__(self):
        self.id = 89
