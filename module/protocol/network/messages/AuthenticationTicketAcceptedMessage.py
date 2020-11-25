from module.protocol.network.message import Message


class AuthenticationTicketAcceptedMessage(Message):
    def __init__(self):
        self.id = 3991
