from module.protocol.network.message import Message


class GuildFightPlayersEnemyRemoveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6792
        self.fightId = {"type": "Number", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
