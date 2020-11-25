from module.protocol.network.message import Message


class GameActionFightKillMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8096
        self.targetId = {"type": "Number", "value": ""}
