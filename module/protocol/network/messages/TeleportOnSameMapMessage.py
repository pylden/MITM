from module.protocol.network.message import Message


class TeleportOnSameMapMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7423
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "uint", "value": ""}
