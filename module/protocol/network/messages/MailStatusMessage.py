from module.protocol.network.message import Message


class MailStatusMessage(Message):
    def __init__(self):
        self.id = 3369
