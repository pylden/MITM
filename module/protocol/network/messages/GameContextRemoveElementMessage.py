from module.protocol.network.message import Message


class GameContextRemoveElementMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 52
        self.id = {"type": "Number", "value": ""}
