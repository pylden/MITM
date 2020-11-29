from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterCreationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1633
        self.vars.append({"name": "name", "type": "String", "value": ""})
        self.vars.append({"name": "breed", "type": "int", "value": ""})
        self.vars.append({"name": "sex", "type": "Boolean", "value": ""})
        self.vars.append({"name": "colors", "type": "Vector.<int>", "value": ""})
        self.vars.append({"name": "cosmeticId", "type": "uint", "value": ""})
