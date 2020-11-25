from module.protocol.network.message import Message


class BreachInvitationOfferMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5041
        self.host = {"type": "CharacterMinimalInformations", "value": ""}
        self.timeLeftBeforeCancel = {"type": "uint", "value": ""}
