from module.protocol.network.message import Message


class AccountLoggingKickedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1881
        self.days = {"type": "uint", "value": ""}
        self.hours = {"type": "uint", "value": ""}
        self.minutes = {"type": "uint", "value": ""}
