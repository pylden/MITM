from module.protocol.network.message import Message


class PartyUpdateLightMessage(Message):
    def __init__(self):
        self.id = 8915
