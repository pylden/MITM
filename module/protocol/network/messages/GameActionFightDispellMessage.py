from module.protocol.network.message import Message


class GameActionFightDispellMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7134
        self.targetId = {"type": "Number", "value": ""}
        self.verboseCast = {"type": "Boolean", "value": ""}
