from module.protocol.network.message import Message


class OrnamentSelectedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7227
        self.ornamentId = {"type": "uint", "value": ""}
