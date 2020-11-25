from module.protocol.network.message import Message


class GameActionFightInvisibilityMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8056
        self.targetId = {"type": "Number", "value": ""}
        self.state = {"type": "uint", "value": ""}
