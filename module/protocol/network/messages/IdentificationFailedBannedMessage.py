from module.protocol.network.message import Message


class IdentificationFailedBannedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7380
        self.banEndDate = {"type": "Number", "value": ""}
