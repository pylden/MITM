from module.protocol.network.message import Message


class ExchangeHandleMountsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3008
        self.actionType = {"type": "int", "value": ""}
        self.ridesId = {"type": "Vector.<uint>", "value": ""}
