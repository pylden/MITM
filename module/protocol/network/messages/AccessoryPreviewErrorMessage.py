from module.protocol.network.message import Message


class AccessoryPreviewErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2799
        self.error = {"type": "uint", "value": ""}
