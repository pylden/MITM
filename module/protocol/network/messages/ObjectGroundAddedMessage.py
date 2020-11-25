from module.protocol.network.message import Message


class ObjectGroundAddedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8648
        self.cellId = {"type": "uint", "value": ""}
        self.objectGID = {"type": "uint", "value": ""}
