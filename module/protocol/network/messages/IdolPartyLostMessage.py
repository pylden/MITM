from module.protocol.network.message import Message


class IdolPartyLostMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2578
        self.idolId = {"type": "uint", "value": ""}
