from module.protocol.network.message import Message


class AccessoryPreviewRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9763
        self.genericId = {"type": "Vector.<uint>", "value": ""}
