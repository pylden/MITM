from module.protocol.network.message import Message


class GameContextRemoveElementMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 52
        self.id = {"type": "Number", "value": ""}
