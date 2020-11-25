from module.protocol.network.message import Message


class ExchangeMountsPaddockAddMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8112
        self.mountDescription = {"type": "Vector.<MountClientData>", "value": ""}
