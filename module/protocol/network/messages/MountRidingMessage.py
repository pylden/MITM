from module.protocol.network.message import Message


class MountRidingMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9431
        self.isRiding = {"type": "Boolean", "value": ""}
        self.isAutopilot = {"type": "Boolean", "value": ""}
