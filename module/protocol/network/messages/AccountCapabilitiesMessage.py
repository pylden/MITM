from module.protocol.network.message import Message


class AccountCapabilitiesMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6878
        self.accountId = {"type": "uint", "value": ""}
        self.tutorialAvailable = {"type": "Boolean", "value": ""}
        self.breedsVisible = {"type": "uint", "value": ""}
        self.breedsAvailable = {"type": "uint", "value": ""}
        self.status = {"type": "int", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
