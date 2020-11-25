from module.protocol.network.message import Message


class ShortcutBarRemoveRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 373
        self.barType = {"type": "uint", "value": ""}
        self.slot = {"type": "uint", "value": ""}
