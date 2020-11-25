from module.protocol.network.message import Message


class GameFightLeaveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8271
        self.charId = {"type": "Number", "value": ""}
