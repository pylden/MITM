from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6642
        self.playerId = {"type": "Number", "value": ""}
        self.monsterGroupId = {"type": "Number", "value": ""}
        self.angryStartTime = {"type": "Number", "value": ""}
        self.attackTime = {"type": "Number", "value": ""}
