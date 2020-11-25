from module.protocol.network.message import Message


class IdentificationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5833
        self.lang = {"type": "String", "value": ""}
