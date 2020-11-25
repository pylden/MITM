from module.protocol.network.message import Message


class AccessoryPreviewErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2799
        self.error = {"type": "uint", "value": ""}
