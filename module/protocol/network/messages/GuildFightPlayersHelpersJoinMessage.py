from module.protocol.network.message import Message


class GuildFightPlayersHelpersJoinMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4515
        self.fightId = {"type": "Number", "value": ""}
        self.playerInfo = {"type": "CharacterMinimalPlusLookInformations", "value": ""}
