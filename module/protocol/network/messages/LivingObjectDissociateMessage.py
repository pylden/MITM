from module.protocol.network.message import Message


class LivingObjectDissociateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6028
        self.livingUID = {"type": "uint", "value": ""}
        self.livingPosition = {"type": "uint", "value": ""}
