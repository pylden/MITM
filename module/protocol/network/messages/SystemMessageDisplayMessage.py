from module.protocol.network.message import Message


class SystemMessageDisplayMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4995
        self.hangUp = {"type": "Boolean", "value": ""}
        self.msgId = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
