from module.protocol.network.message import Message


class CharacterSelectedSuccessMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1931
        self.infos = {"type": "CharacterBaseInformations", "value": ""}
        self.isCollectingStats = {"type": "Boolean", "value": ""}
