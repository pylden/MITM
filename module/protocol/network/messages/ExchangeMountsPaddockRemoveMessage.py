from module.protocol.network.message import Message


class ExchangeMountsPaddockRemoveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9109
        self.mountsId = {"type": "Vector.<int>", "value": ""}
