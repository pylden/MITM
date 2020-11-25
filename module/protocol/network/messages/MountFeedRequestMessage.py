from module.protocol.network.message import Message


class MountFeedRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1812
        self.mountUid = {"type": "uint", "value": ""}
        self.mountLocation = {"type": "int", "value": ""}
        self.mountFoodUid = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
