from module.protocol.network.message import Message


class GameRolePlayShowChallengeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5095
        self.commonsInfos = {"type": "FightCommonInformations", "value": ""}
