from module.protocol.network.message import Message


class ContactLookRequestByIdMessage(Message):
    def __init__(self):
        self.id = 4004
