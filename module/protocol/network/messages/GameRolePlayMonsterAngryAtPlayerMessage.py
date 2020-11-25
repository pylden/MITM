from module.protocol.network.message import Message


class GameRolePlayMonsterAngryAtPlayerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6642
        self.playerId = {"type": "Number", "value": ""}
        self.monsterGroupId = {"type": "Number", "value": ""}
        self.angryStartTime = {"type": "Number", "value": ""}
        self.attackTime = {"type": "Number", "value": ""}
