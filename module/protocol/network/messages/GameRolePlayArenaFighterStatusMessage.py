from module.protocol.network.message import Message


class GameRolePlayArenaFighterStatusMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7701
        self.fightId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.accepted = {"type": "Boolean", "value": ""}
