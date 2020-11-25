from module.protocol.network.message import Message


class StatedElementUpdatedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4169
        self.statedElement = {"type": "StatedElement", "value": ""}
