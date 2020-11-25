from module.protocol.network.message import Message


class AuthenticationTicketMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8374
        self.lang = {"type": "String", "value": ""}
        self.ticket = {"type": "String", "value": ""}
