from module.protocol.network.messages.CharacterSelectionMessage import CharacterSelectionMessage


class CharacterFirstSelectionMessage(CharacterSelectionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CharacterSelectionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1228
        self.doTutorial = {"type": "Boolean", "value": ""}
