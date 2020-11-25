from module.protocol.network.message import Message


class ExchangeBidHouseInListRemovedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6283
        self.itemUID = {"type": "int", "value": ""}
        self.objectGID = {"type": "uint", "value": ""}
        self.objectType = {"type": "uint", "value": ""}
