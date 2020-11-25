from module.protocol.network.message import Message


class GuildFightPlayersEnemyRemoveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6792
        self.fightId = {"type": "Number", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
