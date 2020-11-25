from module.protocol.network.message import Message


class OrnamentGainedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3842
        self.ornamentId = {"type": "uint", "value": ""}
