from module.protocol.network.message import Message


class GameRolePlayArenaFighterStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7701
        self.fightId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.accepted = {"type": "Boolean", "value": ""}
