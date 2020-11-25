from module.protocol.network.message import Message


class GameContextCreateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7391
        self.context = {"type": "uint", "value": ""}
