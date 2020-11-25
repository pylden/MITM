from module.protocol.network.message import Message


class PartyRestrictedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2491
        self.restricted = {"type": "Boolean", "value": ""}
