from module.protocol.network.message import Message


class OrnamentSelectRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7916
        self.ornamentId = {"type": "uint", "value": ""}
