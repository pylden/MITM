from module.protocol.network.message import Message


class IdolSelectRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7388
        self.idolId = {"type": "uint", "value": ""}
        self.activate = {"type": "Boolean", "value": ""}
        self.party = {"type": "Boolean", "value": ""}
