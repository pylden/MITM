from module.protocol.network.message import Message


class BreachInvitationCloseMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 608
        self.host = {"type": "CharacterMinimalInformations", "value": ""}
