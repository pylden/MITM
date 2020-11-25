from module.protocol.network.message import Message


class BasicPongMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5053
        self.quiet = {"type": "Boolean", "value": ""}
