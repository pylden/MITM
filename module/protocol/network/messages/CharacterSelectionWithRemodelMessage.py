from module.protocol.network.messages.CharacterSelectionMessage import CharacterSelectionMessage


class CharacterSelectionWithRemodelMessage(CharacterSelectionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CharacterSelectionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5795
        self.remodel = {"type": "RemodelingInformation", "value": ""}
