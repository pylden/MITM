from module.protocol.network.message import Message


class LivingObjectMessageMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9436
        self.msgId = {"type": "uint", "value": ""}
        self.timeStamp = {"type": "uint", "value": ""}
        self.owner = {"type": "String", "value": ""}
        self.objectGenericId = {"type": "uint", "value": ""}
