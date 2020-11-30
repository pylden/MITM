from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AccountCapabilitiesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6878
        self.accountId = {"type": "uint", "value": ""}
        self.tutorialAvailable = {"type": "Boolean", "value": ""}
        self.breedsVisible = {"type": "uint", "value": ""}
        self.breedsAvailable = {"type": "uint", "value": ""}
        self.status = {"type": "int", "value": ""}
        self.canCreateNewCharacter = {"type": "Boolean", "value": ""}
