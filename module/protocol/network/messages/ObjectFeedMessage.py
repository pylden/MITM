from module.protocol.network.message import Message


class ObjectFeedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5627
        self.objectUID = {"type": "uint", "value": ""}
        self.meal = {"type": "Vector.<ObjectItemQuantity>", "value": ""}
