from module.protocol.network.message import Message


class ShortcutBarContentMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 400
        self.barType = {"type": "uint", "value": ""}
        self.shortcuts = {"type": "Vector.<Shortcut>", "value": ""}
