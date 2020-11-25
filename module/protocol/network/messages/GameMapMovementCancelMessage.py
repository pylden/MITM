from module.protocol.network.message import Message


class GameMapMovementCancelMessage(Message):
    def __init__(self):
        self.id = 615
