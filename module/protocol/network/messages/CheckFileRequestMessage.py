from module.protocol.network.message import Message


class CheckFileRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4509
        self.filename = {"type": "String", "value": ""}
