from module.protocol.network.message import Message


class BasicWhoAmIRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5576
        self.verbose = {"type": "Boolean", "value": ""}
