from module.protocol.network.message import Message


class GameRolePlayArenaFightPropositionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5355
        self.fightId = {"type": "uint", "value": ""}
        self.alliesId = {"type": "Vector.<Number>", "value": ""}
        self.duration = {"type": "uint", "value": ""}
