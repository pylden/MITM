from module.protocol.network.message import Message


class ExchangeMountsStableAddMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9398
        self.mountDescription = {"type": "Vector.<MountClientData>", "value": ""}
