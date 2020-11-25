from module.protocol.network.message import Message


class WarnOnPermaDeathMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3362
        self.enable = {"type": "Boolean", "value": ""}
