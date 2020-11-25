from module.protocol.network.message import Message


class GameFightTurnListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 399
        self.ids = {"type": "Vector.<Number>", "value": ""}
        self.deadsIds = {"type": "Vector.<Number>", "value": ""}
