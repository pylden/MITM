from module.protocol.network.message import Message


class MountRidingMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9431
        self.isRiding = {"type": "Boolean", "value": ""}
        self.isAutopilot = {"type": "Boolean", "value": ""}
