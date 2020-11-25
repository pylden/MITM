from module.protocol.network.message import Message


class GuildFightPlayersHelpersLeaveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2966
        self.fightId = {"type": "Number", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
