from module.protocol.network.message import Message


class GuildFightPlayersEnemiesListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1605
        self.fightId = {"type": "Number", "value": ""}
        self.playerInfo = {"type": "Vector.<CharacterMinimalPlusLookInformations>", "value": ""}
