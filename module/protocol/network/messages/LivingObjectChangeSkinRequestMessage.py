from module.protocol.network.message import Message


class LivingObjectChangeSkinRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1423
        self.livingUID = {"type": "uint", "value": ""}
        self.livingPosition = {"type": "uint", "value": ""}
        self.skinId = {"type": "uint", "value": ""}
