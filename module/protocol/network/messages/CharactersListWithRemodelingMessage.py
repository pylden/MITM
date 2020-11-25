from module.protocol.network.message import Message


class CharactersListWithRemodelingMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1644
        self.charactersToRemodel = {"type": "Vector.<CharacterToRemodelInformations>", "value": ""}
