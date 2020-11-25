from module.protocol.network.message import Message


class ExchangeMountsStableRemoveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9478
        self.mountsId = {"type": "Vector.<int>", "value": ""}
