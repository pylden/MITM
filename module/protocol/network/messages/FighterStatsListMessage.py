from module.protocol.network.message import Message


class FighterStatsListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6334
        self.stats = {"type": "CharacterCharacteristicsInformations", "value": ""}
