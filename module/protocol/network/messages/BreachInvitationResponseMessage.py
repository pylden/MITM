from module.protocol.network.message import Message


class BreachInvitationResponseMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7771
        self.guest = {"type": "CharacterMinimalInformations", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
