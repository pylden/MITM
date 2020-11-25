from module.protocol.network.message import Message


class PartyModifiableStatusMessage(Message):
    def __init__(self):
        self.id = 7012
