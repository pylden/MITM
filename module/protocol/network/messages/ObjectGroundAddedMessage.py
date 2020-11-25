from module.protocol.network.message import Message


class ObjectGroundAddedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8648
        self.cellId = {"type": "uint", "value": ""}
        self.objectGID = {"type": "uint", "value": ""}
