from module.protocol.network.message import Message


class MimicryObjectPreviewMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1082
        self.result = {"type": "ObjectItem", "value": ""}
