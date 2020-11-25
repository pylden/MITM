from module.protocol.network.message import Message


class GuildFightPlayersHelpersJoinMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4515
        self.fightId = {"type": "Number", "value": ""}
        self.playerInfo = {"type": "CharacterMinimalPlusLookInformations", "value": ""}
