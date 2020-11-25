from module.protocol.network.message import Message


class BreachInvitationResponseMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7771
        self.guest = {"type": "CharacterMinimalInformations", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
