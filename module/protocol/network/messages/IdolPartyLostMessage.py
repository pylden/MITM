from module.protocol.network.message import Message


class IdolPartyLostMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2578
        self.idolId = {"type": "uint", "value": ""}
