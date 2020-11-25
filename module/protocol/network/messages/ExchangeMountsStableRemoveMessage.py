from module.protocol.network.message import Message


class ExchangeMountsStableRemoveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9478
        self.mountsId = {"type": "Vector.<int>", "value": ""}
