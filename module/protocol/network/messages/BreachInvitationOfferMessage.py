from module.protocol.network.message import Message


class BreachInvitationOfferMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5041
        self.host = {"type": "CharacterMinimalInformations", "value": ""}
        self.timeLeftBeforeCancel = {"type": "uint", "value": ""}
