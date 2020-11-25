from module.protocol.network.message import Message


class AccountCapabilitiesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6878
        self.accountId = {"type": "uint", "value": ""}
        self.tutorialAvailable = {"type": "Boolean", "value": ""}
        self.breedsVisible = {"type": "uint", "value": ""}
        self.breedsAvailable = {"type": "uint", "value": ""}
        self.status = {"type": "int", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
