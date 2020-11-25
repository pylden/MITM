from module.protocol.network.message import Message


class InteractiveUsedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9839
        self.entityId = {"type": "Number", "value": ""}
        self.elemId = {"type": "uint", "value": ""}
        self.skillId = {"type": "uint", "value": ""}
        self.duration = {"type": "uint", "value": ""}
        self.canMove = {"type": "Boolean", "value": ""}
