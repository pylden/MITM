from module.protocol.network.message import Message


class GameMapChangeOrientationsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1921
        self.orientations = {"type": "Vector.<ActorOrientation>", "value": ""}
