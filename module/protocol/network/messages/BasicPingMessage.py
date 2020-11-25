from module.protocol.network.message import Message


class BasicPingMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9489
        self.quiet = {"type": "Boolean", "value": ""}
