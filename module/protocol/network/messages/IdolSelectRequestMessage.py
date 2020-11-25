from module.protocol.network.message import Message


class IdolSelectRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7388
        self.idolId = {"type": "uint", "value": ""}
        self.activate = {"type": "Boolean", "value": ""}
        self.party = {"type": "Boolean", "value": ""}
