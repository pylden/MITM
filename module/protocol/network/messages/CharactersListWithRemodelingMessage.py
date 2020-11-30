from module.protocol.network.messages.CharactersListMessage import CharactersListMessage


class CharactersListWithRemodelingMessage(CharactersListMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CharactersListMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1644
        self.charactersToRemodel = {"type": "Vector.<CharacterToRemodelInformations>", "value": ""}
