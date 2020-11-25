from module.protocol.network.message import Message


class GuestModeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3850
        self.active = {"type": "Boolean", "value": ""}
