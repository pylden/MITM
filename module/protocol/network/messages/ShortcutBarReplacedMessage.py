from module.protocol.network.message import Message


class ShortcutBarReplacedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6910
        self.barType = {"type": "uint", "value": ""}
        self.shortcut = {"type": "Shortcut", "value": ""}
