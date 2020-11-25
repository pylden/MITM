from module.protocol.network.message import Message


class AbstractPartyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 555
        self.partyId = {"type": "uint", "value": ""}
