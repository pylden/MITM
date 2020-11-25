from module.protocol.network.message import Message


class GameActionFightDispellMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7134
        self.targetId = {"type": "Number", "value": ""}
        self.verboseCast = {"type": "Boolean", "value": ""}
