from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayMonsterAngryAtPlayerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6642
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
        self.vars.append({"name": "monsterGroupId", "type": "Number", "value": ""})
        self.vars.append({"name": "angryStartTime", "type": "Number", "value": ""})
        self.vars.append({"name": "attackTime", "type": "Number", "value": ""})
