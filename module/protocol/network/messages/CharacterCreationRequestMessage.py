from module.protocol.network.message import Message


class CharacterCreationRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1633
        self.name = {"type": "String", "value": ""}
        self.breed = {"type": "int", "value": ""}
        self.sex = {"type": "Boolean", "value": ""}
        self.colors = {"type": "Vector.<int>", "value": ""}
        self.cosmeticId = {"type": "uint", "value": ""}
