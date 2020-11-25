from module.protocol.network.message import Message


class ContactLookRequestByIdMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4004
        self.playerId = {"type": "Number", "value": ""}
