from module.protocol.network.message import Message


class ContactLookRequestMessage(Message):
    def __init__(self):
        self.id = 4354
