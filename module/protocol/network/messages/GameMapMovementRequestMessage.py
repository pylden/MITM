from module.protocol.network.message import Message


class GameMapMovementRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7064
        self.keyMovements = {"type": "Vector.<uint>", "value": ""}
        self.mapId = {"type": "Number", "value": ""}
