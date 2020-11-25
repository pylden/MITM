from module.protocol.network.message import Message


class ObjectMovementMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3380
        self.objectUID = {"type": "uint", "value": ""}
        self.position = {"type": "uint", "value": ""}
