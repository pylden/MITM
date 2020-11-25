from module.protocol.network.message import Message


class MapFightStartPositionsUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6209
        self.mapId = {"type": "Number", "value": ""}
        self.fightStartPositions = {"type": "FightStartingPositions", "value": ""}
