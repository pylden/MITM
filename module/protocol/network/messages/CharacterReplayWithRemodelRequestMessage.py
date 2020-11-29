from module.protocol.network.messages.CharacterReplayRequestMessage import CharacterReplayRequestMessage


class CharacterReplayWithRemodelRequestMessage(CharacterReplayRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CharacterReplayRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9190
        self.vars.append({"name": "remodel", "type": "RemodelingInformation", "value": ""})
