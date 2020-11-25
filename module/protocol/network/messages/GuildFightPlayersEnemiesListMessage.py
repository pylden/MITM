from module.protocol.network.message import Message


class GuildFightPlayersEnemiesListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1605
        self.fightId = {"type": "Number", "value": ""}
        self.playerInfo = {"type": "Vector.<CharacterMinimalPlusLookInformations>", "value": ""}
