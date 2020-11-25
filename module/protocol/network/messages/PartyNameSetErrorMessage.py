from module.protocol.network.message import Message


class PartyNameSetErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 89
        self.result = {"type": "uint", "value": ""}
