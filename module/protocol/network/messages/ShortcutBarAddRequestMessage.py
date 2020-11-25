from module.protocol.network.message import Message


class ShortcutBarAddRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2373
        self.barType = {"type": "uint", "value": ""}
        self.shortcut = {"type": "Shortcut", "value": ""}
