from module.protocol.network.message import Message


class TextInformationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5636
        self.msgType = {"type": "uint", "value": ""}
        self.msgId = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
