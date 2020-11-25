from module.protocol.network.message import Message


class ExchangeBidHouseInListAddedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9210
        self.itemUID = {"type": "int", "value": ""}
        self.objectGID = {"type": "uint", "value": ""}
        self.objectType = {"type": "uint", "value": ""}
        self.effects = {"type": "Vector.<ObjectEffect>", "value": ""}
        self.prices = {"type": "Vector.<Number>", "value": ""}
