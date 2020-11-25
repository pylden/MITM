from module.protocol.network.message import Message


class GameRolePlayMonsterNotAngryAtPlayerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1541
        self.playerId = {"type": "Number", "value": ""}
        self.monsterGroupId = {"type": "Number", "value": ""}
