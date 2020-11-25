from module.protocol.network.message import Message


class GameActionFightTackledMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8815
        self.tacklersIds = {"type": "Vector.<Number>", "value": ""}
