from module.protocol.network.message import Message


class AuthenticationTicketMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8374
        self.lang = {"type": "String", "value": ""}
        self.ticket = {"type": "String", "value": ""}
