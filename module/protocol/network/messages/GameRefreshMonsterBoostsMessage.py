from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRefreshMonsterBoostsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1992
        self.vars.append({"name": "monsterBoosts", "type": "Vector.<MonsterBoosts>", "value": ""})
        self.vars.append({"name": "familyBoosts", "type": "Vector.<MonsterBoosts>", "value": ""})
