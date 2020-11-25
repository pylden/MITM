from module.protocol.network.message import Message


class ObjectSetPositionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1317
        self.objectUID = {"type": "uint", "value": ""}
        self.position = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
