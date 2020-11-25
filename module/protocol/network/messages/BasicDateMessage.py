from module.protocol.network.message import Message


class BasicDateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4547
        self.day = {"type": "uint", "value": ""}
        self.month = {"type": "uint", "value": ""}
        self.year = {"type": "uint", "value": ""}
