from module.protocol.network.message import Message


class BasicStatMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9271
        self.timeSpent = {"type": "Number", "value": ""}
        self.statId = {"type": "uint", "value": ""}
