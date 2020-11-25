from module.protocol.network.message import Message


class GameActionFightSummonMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2182
        self.summons = {"type": "Vector.<GameFightFighterInformations>", "value": ""}
