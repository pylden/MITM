from module.protocol.network.message import Message


class BreachInvitationCloseMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 608
        self.host = {"type": "CharacterMinimalInformations", "value": ""}
