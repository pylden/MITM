from module.protocol.network.message import Message


class ObjectDropMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5169
        self.objectUID = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
