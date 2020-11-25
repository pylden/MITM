from module.protocol.network.message import Message


class BasicWhoIsNoMatchMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5493
        self.search = {"type": "String", "value": ""}
