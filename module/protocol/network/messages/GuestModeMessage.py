from module.protocol.network.message import Message


class GuestModeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3850
        self.active = {"type": "Boolean", "value": ""}
