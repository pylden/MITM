from module.protocol.network.message import Message


class BasicCharactersListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3322
        self.characters = {"type": "Vector.<CharacterBaseInformations>", "value": ""}
