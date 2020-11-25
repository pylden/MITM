from module.protocol.network.message import Message


class GameMapMovementMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8712
        self.keyMovements = {"type": "Vector.<uint>", "value": ""}
        self.forcedDirection = {"type": "int", "value": ""}
        self.actorId = {"type": "Number", "value": ""}
