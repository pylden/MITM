from module.protocol.network.message import Message


class BreachInvitationAnswerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6890
        self.accept = {"type": "Boolean", "value": ""}
