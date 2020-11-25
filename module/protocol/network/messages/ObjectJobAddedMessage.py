from module.protocol.network.message import Message


class ObjectJobAddedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 355
        self.jobId = {"type": "uint", "value": ""}
