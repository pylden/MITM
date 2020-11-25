from module.protocol.network.message import Message


class GameFightLeaveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8271
        self.charId = {"type": "Number", "value": ""}
