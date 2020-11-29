from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayAttackMonsterRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3866
        self.vars.append({"name": "monsterGroupId", "type": "Number", "value": ""})
