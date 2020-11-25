from module.protocol.network.message import Message


class CharacterStatsListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8872
        self.stats = {"type": "CharacterCharacteristicsInformations", "value": ""}
