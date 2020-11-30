from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterCreationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1633
        self.name = {"type": "String", "value": ""}
        self.breed = {"type": "int", "value": ""}
        self.sex = {"type": "Boolean", "value": ""}
        self.colors = {"type": "Vector.<int>", "value": ""}
        self.cosmeticId = {"type": "uint", "value": ""}
