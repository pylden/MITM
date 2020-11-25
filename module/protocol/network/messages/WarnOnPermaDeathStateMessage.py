from module.protocol.network.message import Message


class WarnOnPermaDeathStateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2119
        self.enable = {"type": "Boolean", "value": ""}
