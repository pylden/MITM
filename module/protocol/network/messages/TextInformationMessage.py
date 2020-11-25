from module.protocol.network.message import Message


class TextInformationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5636
        self.msgType = {"type": "uint", "value": ""}
        self.msgId = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
