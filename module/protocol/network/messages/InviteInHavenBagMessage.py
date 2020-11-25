from module.protocol.network.message import Message


class InviteInHavenBagMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9753
        self.guestInformations = {"type": "CharacterMinimalInformations", "value": ""}
        self.accept = {"type": "Boolean", "value": ""}
