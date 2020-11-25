from module.protocol.network.message import Message


class ExchangeStartOkMountWithOutPaddockMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8908
        self.stabledMountsDescription = {"type": "Vector.<MountClientData>", "value": ""}
