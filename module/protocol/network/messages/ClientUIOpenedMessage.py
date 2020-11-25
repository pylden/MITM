from module.protocol.network.message import Message


class ClientUIOpenedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1056
        self.type = {"type": "uint", "value": ""}
