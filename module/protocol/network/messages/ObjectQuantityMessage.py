from module.protocol.network.message import Message


class ObjectQuantityMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9459
        self.objectUID = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
        self.origin = {"type": "uint", "value": ""}
