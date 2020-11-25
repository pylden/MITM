from module.protocol.network.message import Message


class MountFeedRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1812
        self.mountUid = {"type": "uint", "value": ""}
        self.mountLocation = {"type": "int", "value": ""}
        self.mountFoodUid = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
