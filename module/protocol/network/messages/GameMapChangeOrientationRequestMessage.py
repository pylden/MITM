from module.protocol.network.message import Message


class GameMapChangeOrientationRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1337
        self.direction = {"type": "uint", "value": ""}
