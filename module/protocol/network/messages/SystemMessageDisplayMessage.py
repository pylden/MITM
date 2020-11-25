from module.protocol.network.message import Message


class SystemMessageDisplayMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4995
        self.hangUp = {"type": "Boolean", "value": ""}
        self.msgId = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
