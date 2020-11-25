from module.protocol.network.message import Message


class GameContextKickMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7244
        self.targetId = {"type": "Number", "value": ""}
