from module.protocol.network.message import Message


class IdolPartyRegisterRequestMessage(Message):
    def __init__(self):
        self.id = 5600
