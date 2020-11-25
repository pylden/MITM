from module.protocol.network.message import Message


class BreachInvitationCloseMessage(Message):
    def __init__(self):
        self.id = 608
