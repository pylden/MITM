from module.protocol.network.message import Message


class ShortcutBarRemovedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3974
        self.barType = {"type": "uint", "value": ""}
        self.slot = {"type": "uint", "value": ""}
