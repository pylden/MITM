from module.protocol.network.message import Message


class GameRolePlayArenaFightPropositionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5355
        self.fightId = {"type": "uint", "value": ""}
        self.alliesId = {"type": "Vector.<Number>", "value": ""}
        self.duration = {"type": "uint", "value": ""}
