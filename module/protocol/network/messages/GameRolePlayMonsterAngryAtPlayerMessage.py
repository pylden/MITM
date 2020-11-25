from module.protocol.network.message import Message


class GameRolePlayMonsterAngryAtPlayerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6642
        self.playerId = {"type": "Number", "value": ""}
        self.monsterGroupId = {"type": "Number", "value": ""}
        self.angryStartTime = {"type": "Number", "value": ""}
        self.attackTime = {"type": "Number", "value": ""}
