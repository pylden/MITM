from module.protocol.network.message import Message


class GameMapNoMovementMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6980
        self.cellX = {"type": "int", "value": ""}
        self.cellY = {"type": "int", "value": ""}
