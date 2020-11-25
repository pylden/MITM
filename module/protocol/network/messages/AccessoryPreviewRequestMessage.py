from module.protocol.network.message import Message


class AccessoryPreviewRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9763
        self.genericId = {"type": "Vector.<uint>", "value": ""}
