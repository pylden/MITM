from module.protocol.network.message import Message


class ExchangeStartOkMountMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1272
        self.paddockedMountsDescription = {"type": "Vector.<MountClientData>", "value": ""}
