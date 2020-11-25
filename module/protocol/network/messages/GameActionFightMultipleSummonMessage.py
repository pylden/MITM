from module.protocol.network.message import Message


class GameActionFightMultipleSummonMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4979
        self.summons = {"type": "Vector.<GameContextSummonsInformation>", "value": ""}
