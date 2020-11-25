from module.protocol.network.message import Message


class GameFightPlacementPossiblePositionsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8748
        self.positionsForChallengers = {"type": "Vector.<uint>", "value": ""}
        self.positionsForDefenders = {"type": "Vector.<uint>", "value": ""}
        self.teamNumber = {"type": "uint", "value": ""}
