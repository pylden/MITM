from module.protocol.network.message import Message


class HouseBuyRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1326
        self.proposedPrice = {"type": "Number", "value": ""}
