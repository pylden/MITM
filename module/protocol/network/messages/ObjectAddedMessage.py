from module.protocol.network.message import Message


class ObjectAddedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4410
        self.object = {"type": "ObjectItem", "value": ""}
        self.origin = {"type": "uint", "value": ""}
