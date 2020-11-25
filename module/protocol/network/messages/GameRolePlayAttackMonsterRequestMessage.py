from module.protocol.network.message import Message


class GameRolePlayAttackMonsterRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3866
        self.monsterGroupId = {"type": "Number", "value": ""}
