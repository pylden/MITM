from module.protocol.network.message import Message


class GameActionFightSummonMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2182
        self.summons = {"type": "Vector.<GameFightFighterInformations>", "value": ""}
