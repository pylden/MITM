from module.protocol.network.message import Message


class ShortcutBarContentMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 400
        self.barType = {"type": "uint", "value": ""}
        self.shortcuts = {"type": "Vector.<Shortcut>", "value": ""}
