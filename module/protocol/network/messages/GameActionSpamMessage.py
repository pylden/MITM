from module.protocol.network.message import Message


class GameActionSpamMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1035
        self.cells = {"type": "Vector.<int>", "value": ""}
