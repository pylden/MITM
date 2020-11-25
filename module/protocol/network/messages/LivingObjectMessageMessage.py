from module.protocol.network.message import Message


class LivingObjectMessageMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9436
        self.owner = {"type": "String", "value": ""}
