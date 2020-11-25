from module.protocol.network.message import Message


class MailStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3369
        self.unread = {"type": "uint", "value": ""}
        self.total = {"type": "uint", "value": ""}
