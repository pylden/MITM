from module.protocol.network.message import Message


class ExchangeMountsPaddockRemoveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9109
        self.mountsId = {"type": "Vector.<int>", "value": ""}
