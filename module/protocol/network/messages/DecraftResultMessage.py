from module.protocol.network.message import Message


class DecraftResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8523
        self.results = {"type": "Vector.<DecraftedItemStackInfo>", "value": ""}
