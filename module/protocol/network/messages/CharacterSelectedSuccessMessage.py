from module.protocol.network.message import Message


class CharacterSelectedSuccessMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1931
        self.infos = {"type": "CharacterBaseInformations", "value": ""}
        self.isCollectingStats = {"type": "Boolean", "value": ""}
