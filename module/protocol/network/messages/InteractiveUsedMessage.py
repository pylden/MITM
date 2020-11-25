from module.protocol.network.message import Message


class InteractiveUsedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9839
        self.entityId = {"type": "Number", "value": ""}
        self.elemId = {"type": "uint", "value": ""}
        self.skillId = {"type": "uint", "value": ""}
        self.duration = {"type": "uint", "value": ""}
        self.canMove = {"type": "Boolean", "value": ""}
