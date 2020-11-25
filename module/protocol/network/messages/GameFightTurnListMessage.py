from module.protocol.network.message import Message


class GameFightTurnListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 399
        self.ids = {"type": "Vector.<Number>", "value": ""}
        self.deadsIds = {"type": "Vector.<Number>", "value": ""}
