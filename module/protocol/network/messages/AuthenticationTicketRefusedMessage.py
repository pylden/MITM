from module.protocol.network.message import Message


class AuthenticationTicketRefusedMessage(Message):
    def __init__(self):
        self.id = 5915
