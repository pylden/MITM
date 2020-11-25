from module.protocol.network.message import Message


class InviteInHavenBagOfferMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1021
        self.hostInformations = {"type": "CharacterMinimalInformations", "value": ""}
        self.timeLeftBeforeCancel = {"type": "int", "value": ""}
