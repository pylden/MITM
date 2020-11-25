from module.protocol.network.message import Message


class ObjectUseMultipleMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3678
        self.quantity = {"type": "uint", "value": ""}
