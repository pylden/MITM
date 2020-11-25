from module.protocol.network.message import Message


class ExchangeHandleMountsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3008
        self.actionType = {"type": "int", "value": ""}
        self.ridesId = {"type": "Vector.<uint>", "value": ""}
