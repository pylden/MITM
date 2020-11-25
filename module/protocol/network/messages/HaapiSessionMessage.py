from module.protocol.network.message import Message


class HaapiSessionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6833
        self.key = {"type": "String", "value": ""}
