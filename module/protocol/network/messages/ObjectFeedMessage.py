from module.protocol.network.message import Message


class ObjectFeedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5627
        self.objectUID = {"type": "uint", "value": ""}
        self.meal = {"type": "Vector.<ObjectItemQuantity>", "value": ""}
