from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AccountCapabilitiesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6878
        self.vars.append({"name": "accountId", "type": "uint", "value": ""})
        self.vars.append({"name": "tutorialAvailable", "type": "Boolean", "value": ""})
        self.vars.append({"name": "breedsVisible", "type": "uint", "value": ""})
        self.vars.append({"name": "breedsAvailable", "type": "uint", "value": ""})
        self.vars.append({"name": "status", "type": "int", "value": ""})
        self.vars.append({"name": "canCreateNewCharacter", "type": "Boolean", "value": ""})
