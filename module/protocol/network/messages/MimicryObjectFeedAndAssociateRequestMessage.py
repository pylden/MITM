from module.protocol.network.message import Message


class MimicryObjectFeedAndAssociateRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8282
        self.foodUID = {"type": "uint", "value": ""}
        self.foodPos = {"type": "uint", "value": ""}
        self.preview = {"type": "Boolean", "value": ""}
