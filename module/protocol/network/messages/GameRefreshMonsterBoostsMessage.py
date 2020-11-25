from module.protocol.network.message import Message


class GameRefreshMonsterBoostsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1992
        self.monsterBoosts = {"type": "Vector.<MonsterBoosts>", "value": ""}
        self.familyBoosts = {"type": "Vector.<MonsterBoosts>", "value": ""}
