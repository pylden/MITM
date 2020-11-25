from module.protocol.network.message import Message


class QueueStatusMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9955
        self.position = {"type": "uint", "value": ""}
        self.total = {"type": "uint", "value": ""}
