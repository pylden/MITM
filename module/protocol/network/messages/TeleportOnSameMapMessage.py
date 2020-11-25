from module.protocol.network.message import Message


class TeleportOnSameMapMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7423
        self.targetId = {"type": "Number", "value": ""}
        self.cellId = {"type": "uint", "value": ""}
