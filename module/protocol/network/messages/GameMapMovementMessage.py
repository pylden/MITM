from module.protocol.network.message import Message


class GameMapMovementMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8712
        self.keyMovements = {"type": "Vector.<uint>", "value": ""}
        self.forcedDirection = {"type": "int", "value": ""}
        self.actorId = {"type": "Number", "value": ""}
