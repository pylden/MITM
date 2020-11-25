from module.protocol.network.message import Message


class LivingObjectMessageRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4103
        self.msgId = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
        self.livingObject = {"type": "uint", "value": ""}
