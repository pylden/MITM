from module.protocol.network.message import Message


class MimicryObjectPreviewMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1082
        self.result = {"type": "ObjectItem", "value": ""}
