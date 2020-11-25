from module.protocol.network.message import Message


class StatedElementUpdatedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4169
        self.statedElement = {"type": "StatedElement", "value": ""}
