from module.protocol.network.message import Message


class BreachInvitationRequestMessage(Message):
    def __init__(self):
        self.id = 19
