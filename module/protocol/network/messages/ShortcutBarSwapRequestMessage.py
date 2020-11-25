from module.protocol.network.message import Message


class ShortcutBarSwapRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6397
        self.barType = {"type": "uint", "value": ""}
        self.firstSlot = {"type": "uint", "value": ""}
        self.secondSlot = {"type": "uint", "value": ""}
