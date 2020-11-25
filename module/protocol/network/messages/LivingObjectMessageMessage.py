from module.protocol.network.message import Message


class LivingObjectMessageMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9436
        self.msgId = {"type": "uint", "value": ""}
        self.timeStamp = {"type": "uint", "value": ""}
        self.owner = {"type": "String", "value": ""}
        self.objectGenericId = {"type": "uint", "value": ""}
