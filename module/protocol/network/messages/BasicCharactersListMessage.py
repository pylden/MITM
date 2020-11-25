from module.protocol.network.message import Message


class BasicCharactersListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3322
        self.characters = {"type": "Vector.<CharacterBaseInformations>", "value": ""}
