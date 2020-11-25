from module.protocol.network.message import Message


class ExchangeMountsPaddockAddMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8112
        self.mountDescription = {"type": "Vector.<MountClientData>", "value": ""}
