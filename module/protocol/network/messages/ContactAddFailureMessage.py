from module.protocol.network.message import Message


class ContactAddFailureMessage(Message):
    def __init__(self):
        self.id = 2662
