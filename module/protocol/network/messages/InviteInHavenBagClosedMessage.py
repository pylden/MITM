from module.protocol.network.message import Message


class InviteInHavenBagClosedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3445
        self.hostInformations = {"type": "CharacterMinimalInformations", "value": ""}
